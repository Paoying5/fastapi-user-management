import fs from "node:fs";
import path from "node:path";

const webRoot = process.cwd();
const repoRoot = path.resolve(webRoot, "..");

const diaryDir = path.join(repoRoot, "docs", "diary");
const analyticsDir = path.join(repoRoot, "sql", "analytics");

const outputFile = path.join(
  webRoot,
  "src",
  "data",
  "progress.generated.json"
);

function readText(filePath) {
  return fs.readFileSync(filePath, "utf8");
}

function cleanMarkdown(text) {
  return text
    .replace(/`([^`]+)`/g, "$1")
    .replace(/\*\*([^*]+)\*\*/g, "$1")
    .replace(/\[([^\]]+)\]\([^)]+\)/g, "$1")
    .trim();
}

function findLastNumber(text, patterns, fallback) {
  const matches = [];

  for (const pattern of patterns) {
    const globalPattern = new RegExp(
      pattern.source,
      pattern.flags.includes("g")
        ? pattern.flags
        : `${pattern.flags}g`
    );

    for (const match of text.matchAll(globalPattern)) {
      matches.push({
        value: Number(match[1].replaceAll(",", "")),
        index: match.index ?? -1,
      });
    }
  }

  if (matches.length === 0) {
    return fallback;
  }

  matches.sort((a, b) => a.index - b.index);

  return matches.at(-1).value;
}

function extractBullets(markdown, limit = 8) {
  return markdown
    .split("\n")
    .map((line) => line.trim())
    .filter((line) => /^[-*]\s+/.test(line))
    .map((line) => cleanMarkdown(line.replace(/^[-*]\s+/, "")))
    .filter((line) => line.length > 8 && line.length < 150)
    .slice(0, limit);
}

function buildHighlights(markdown, stats) {
  const bullets = extractBullets(markdown, 50);

  const usefulBullets = bullets.filter((line) => {
    const normalized = line.toLowerCase();

    const usefulKeyword =
      normalized.includes("complete") ||
      normalized.includes("completed") ||
      normalized.includes("implement") ||
      normalized.includes("verified") ||
      normalized.includes("migration") ||
      normalized.includes("test") ||
      normalized.includes("analytics") ||
      normalized.includes("dataset") ||
      normalized.includes("sql") ||
      normalized.includes("lifecycle");

    const looksLikeFieldName =
      line.endsWith(";") ||
      /^[a-z0-9_]+;?$/i.test(line);

    return (
      usefulKeyword &&
      !looksLikeFieldName &&
      line.length >= 20 &&
      line.length <= 140
    );
  });

  const unique = [...new Set(usefulBullets)];

  if (unique.length >= 5) {
    return unique.slice(0, 8);
  }

  return [
    "Completed User and Post lifecycle support",
    "Verified authentication and inactive-user lifecycle",
    `Reached ${stats.tests} passing automated tests`,
    `Prepared ${stats.analyticsUsers.toLocaleString()} synthetic analytics users`,
    `Analyzed ${stats.analyticsPosts.toLocaleString()} synthetic posts`,
    "Completed exploratory SQL and KPI analysis",
    "Practiced business-question analysis",
    "Practiced SQL window functions",
  ];
}

function extractWeek(text) {
  const match = text.match(/\bW\d{1,2}\b/i);
  return match ? match[0].toUpperCase() : "Latest";
}

function formatDate(dateString) {
  const date = new Date(`${dateString}T00:00:00Z`);

  return new Intl.DateTimeFormat("en", {
    day: "2-digit",
    month: "short",
    year: "numeric",
    timeZone: "UTC",
  }).format(date);
}

function findLatestDiary() {
  const files = fs
    .readdirSync(diaryDir)
    .filter((name) => name.endsWith(".md"))
    .filter((name) => name !== "README.md");

  const rangedProgressFiles = files
    .filter((name) =>
      /^\d{4}-\d{2}-\d{2}-to-\d{4}-\d{2}-\d{2}-current-progress\.md$/.test(
        name
      )
    )
    .sort();

  const summaryFiles = files
    .filter((name) =>
      /^\d{4}-\d{2}-\d{2}-project-summary\.md$/.test(name)
    )
    .sort();

  const latestProgress =
    rangedProgressFiles.at(-1) ?? null;

  const latestSummary =
    summaryFiles.at(-1) ?? null;

  return {
    latestProgress,
    latestSummary,
  };
}

function buildAnalyticsRoadmap() {
  const files = fs
    .readdirSync(analyticsDir)
    .filter((name) => name.endsWith(".sql"));

  const stages = [
    {
      file: "01_seed_analytics.sql",
      title: "Dataset Preparation",
    },
    {
      file: "02_exploration.sql",
      title: "Exploratory SQL",
    },
    {
      file: "03_kpi_analysis.sql",
      title: "KPI Analysis",
    },
    {
      file: "04_business_questions.sql",
      title: "Business Questions",
    },
    {
      file: "05_window_functions.sql",
      title: "Window Functions",
    },
  ];

  return stages.map((stage) => ({
    ...stage,
    completed: files.includes(stage.file),
  }));
}

const { latestProgress, latestSummary } = findLatestDiary();

if (!latestProgress) {
  throw new Error(
    "No ranged current-progress diary file was found."
  );
}

const progressPath = path.join(
  diaryDir,
  latestProgress
);

const progressMarkdown = readText(progressPath);

const summaryMarkdown = latestSummary
  ? readText(path.join(diaryDir, latestSummary))
  : "";

const combinedText =
  `${progressMarkdown}\n${summaryMarkdown}`;

const rangeMatch = latestProgress.match(
  /^(\d{4}-\d{2}-\d{2})-to-(\d{4}-\d{2}-\d{2})/
);

const startDate = rangeMatch?.[1] ?? null;
const endDate = rangeMatch?.[2] ?? null;

const tests = findLastNumber(
  combinedText,
  [
    /(\d+)\s*\/\s*\d+\s*(?:tests?|test)/i,
    /(\d+)\s+(?:automated\s+)?tests?\s+(?:passed|pass)/i,
  ],
  79
);

const analyticsUsers = findLastNumber(
  combinedText,
  [
    /([\d,]+)\s+synthetic\s+users/i,
    /([\d,]+)\s+analytics\s+users/i,
    /dataset\s+(?:of|with|gồm)\s+([\d,]+)\s+users/i,
    /([\d,]+)\s+users/i,
  ],
  600
);

const analyticsPosts = findLastNumber(
  combinedText,
  [
    /([\d,]+)\s+synthetic\s+posts/i,
    /([\d,]+)\s+analytics\s+posts/i,
    /dataset\s+(?:of|with|gồm)\s+([\d,]+)\s+posts/i,
    /([\d,]+)\s+posts/i,
  ],
  2250
);

const highlights = buildHighlights(
  combinedText,
  {
    tests,
    analyticsUsers,
    analyticsPosts,
  }
);

const analyticsStages = buildAnalyticsRoadmap();

const completedAnalyticsStages =
  analyticsStages.filter(
    (stage) => stage.completed
  ).length;

let currentFocus = "SQL Analytics";

if (
  completedAnalyticsStages ===
  analyticsStages.length
) {
  currentFocus = "Pandas & EDA";
}

const data = {
  generatedAt: new Date().toISOString(),

  latest: {
    week: extractWeek(combinedText),

    startDate,

    endDate,

    period:
      startDate && endDate
        ? `${formatDate(startDate)} — ${formatDate(endDate)}`
        : "Latest progress",

    progressFile: latestProgress,

    summaryFile: latestSummary,

    highlights,
  },

  stats: {
    tests,
    analyticsUsers,
    analyticsPosts,

    postingRate: 80,

    topCreatorShare: 38.67,
  },

  currentFocus,

  analyticsStages,
};

fs.writeFileSync(
  outputFile,
  `${JSON.stringify(data, null, 2)}\n`
);

console.log("✓ Mentor progress data synchronized");
console.log(`  Diary: ${latestProgress}`);
console.log(
  `  Analytics stages: ${completedAnalyticsStages}/${analyticsStages.length}`
);
console.log(`  Current focus: ${currentFocus}`);