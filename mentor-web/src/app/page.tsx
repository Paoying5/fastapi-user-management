
"use client";

import { useMemo, useState } from "react";
import {
  Activity,
  ArrowDownRight,
  ArrowUpRight,
  BarChart3,
  CheckCircle2,
  ChevronRight,
  CircleHelp,
  Database,
  FileText,
  Globe2,
  LayoutDashboard,
  Moon,
  ShieldCheck,
  Sun,
  Target,
  TrendingUp,
  Users,
} from "lucide-react";

import {
  Bar,
  BarChart,
  CartesianGrid,
  Cell,
  Pie,
  PieChart,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis,
} from "recharts";

import progress from "@/data/progress.generated.json";

type Language = "en" | "vi";
type Theme = "light" | "dark";
type Period = "all" | "6" | "3";

type MonthlyPoint = {
  month: string;
  posts: number;
};

const monthlyPosts = progress.monthlyPosts as MonthlyPoint[];

const translations = {
  en: {
    workspace: "ANALYTICS WORKSPACE",
    dashboard: "Dashboard",
    overview: "Overview",
    storytelling: "Data storytelling",
    questions: "Business questions",
    quality: "Data quality",
    portfolio: "DATA ANALYST PORTFOLIO",
    title: "Social Content Analytics",
    subtitle:
      "Explore user participation, content activity, and publishing behavior.",
    sample: "Synthetic dataset",
    lastUpdated: "Reporting period",
    allTime: "All months",
    last6: "Last 6 months",
    last3: "Last 3 months",
    users: "Total users",
    activeUsers: "Users who posted",
    participation: "Participation rate",
    totalPosts: "Posts in selected period",
    ofUsers: "of total users",
    havePosted: "have created at least one post",
    engagement: "user participation",
    periodPosts: "posts in selected period",
    monthlyTitle: "Monthly publishing activity",
    monthlySubtitle: "Number of posts created each month",
    posts: "Posts",
    selectedTotal: "Total across displayed months",
    statusTitle: "Content status distribution",
    statusSubtitle: "Share of posts by current status",
    published: "Published",
    draft: "Draft",
    archived: "Archived",
    storytellingTitle: "What the data tells us",
    storytellingSubtitle:
      "Each finding includes an interpretation and a limitation.",
    finding1Title: "Most users have contributed content",
    finding1:
      "480 of 600 users have created at least one post, giving the dataset an 80% posting-user rate.",
    finding1Meaning:
      "Interpretation: content creation is distributed across a large share of the user base.",
    finding1Limit:
      "Limitation: posting at least once does not necessarily mean a user is currently active.",
    finding2Title: "A small creator group contributes a large share",
    finding2:
      "The top 10% of creators account for 38.67% of all posts in the dataset.",
    finding2Meaning:
      "Interpretation: a relatively small group contributes a substantial share of content.",
    finding2Limit:
      "Limitation: this metric alone does not establish why those users create more content.",
    finding3Title: "Publishing activity changes over time",
    questionsTitle: "Business questions to investigate",
    questionsSubtitle:
      "A practical analysis workflow starts with a question, evidence, and a next step.",
    question: "Business question",
    evidence: "Current evidence",
    nextStep: "Suggested next analysis",
    q1: "How many users contribute content?",
    e1: "480 of 600 users have posted at least once.",
    n1: "Compare new, returning, and inactive users over time.",
    q2: "How concentrated is content creation?",
    e2: "The top 10% of creators produce 38.67% of posts.",
    n2: "Calculate creator percentiles and compare posting frequency groups.",
    q3: "When is publishing activity highest?",
    n3: "Compare complete months and investigate seasonality before drawing conclusions.",
    q4: "What happens between draft and published status?",
    e4: "Current status shares are 70% published, 20% draft, and 10% archived.",
    n4: "Use status-change timestamps to measure publication conversion and time to publish.",
    qualityTitle: "Data quality and methodology",
    qualitySubtitle:
      "Document what the dataset can and cannot support before making recommendations.",
    source: "Data source",
    sourceValue: "Generated synthetic analytics dataset",
    scope: "Dataset scope",
    completeness: "Time coverage",
    caveat: "Important caveat",
    caveatValue:
      "The latest month may be incomplete. Monthly comparisons should use complete months only.",
    limitation: "Analysis limitation",
    limitationValue:
      "Current status shares do not reveal the transition from draft to published without lifecycle timestamps.",
    workflow: "Analyst workflow",
    step1: "Define a business question",
    step2: "Validate the data and its scope",
    step3: "Explore patterns and compare groups",
    step4: "Explain findings and limitations",
    step5: "Recommend the next analysis",
    footer:
      "Portfolio project · Synthetic data · Findings are descriptive, not causal",
    themeLight: "Light mode",
    themeDark: "Dark mode",
    language: "Language",
    periodLabel: "Time period",
    noData: "No monthly data available.",
  },
  vi: {
    workspace: "KHÔNG GIAN PHÂN TÍCH",
    dashboard: "Dashboard",
    overview: "Tổng quan",
    storytelling: "Kể chuyện bằng dữ liệu",
    questions: "Câu hỏi kinh doanh",
    quality: "Chất lượng dữ liệu",
    portfolio: "DỰ ÁN DATA ANALYST",
    title: "Phân tích nội dung mạng xã hội",
    subtitle:
      "Khám phá mức độ tham gia của người dùng, hoạt động tạo bài đăng và hành vi xuất bản.",
    sample: "Dữ liệu mô phỏng",
    lastUpdated: "Khoảng thời gian",
    allTime: "Tất cả tháng",
    last6: "6 tháng gần nhất",
    last3: "3 tháng gần nhất",
    users: "Tổng số người dùng",
    activeUsers: "Người dùng đã đăng bài",
    participation: "Tỷ lệ tham gia",
    totalPosts: "Bài đăng trong kỳ",
    ofUsers: "trên tổng người dùng",
    havePosted: "đã tạo ít nhất một bài đăng",
    engagement: "tỷ lệ tham gia tạo nội dung",
    periodPosts: "bài đăng trong kỳ đã chọn",
    monthlyTitle: "Hoạt động đăng bài theo tháng",
    monthlySubtitle: "Số lượng bài đăng được tạo trong từng tháng",
    posts: "Bài đăng",
    selectedTotal: "Tổng bài đăng trong các tháng đang hiển thị",
    statusTitle: "Phân bố trạng thái nội dung",
    statusSubtitle: "Tỷ trọng bài đăng theo trạng thái hiện tại",
    published: "Đã xuất bản",
    draft: "Bản nháp",
    archived: "Đã lưu trữ",
    storytellingTitle: "Dữ liệu đang cho chúng ta biết điều gì?",
    storytellingSubtitle:
      "Mỗi phát hiện đều đi kèm diễn giải và giới hạn của dữ liệu.",
    finding1Title: "Phần lớn người dùng đã đóng góp nội dung",
    finding1:
      "480 trong số 600 người dùng đã tạo ít nhất một bài đăng, tương đương tỷ lệ 80%.",
    finding1Meaning:
      "Diễn giải: hoạt động tạo nội dung xuất hiện ở một tỷ lệ lớn trong tập người dùng.",
    finding1Limit:
      "Giới hạn: từng đăng bài ít nhất một lần không đồng nghĩa người dùng vẫn đang hoạt động.",
    finding2Title: "Một nhóm nhỏ tạo ra tỷ trọng nội dung đáng kể",
    finding2:
      "Nhóm 10% người tạo nội dung nhiều nhất đóng góp 38,67% tổng số bài đăng.",
    finding2Meaning:
      "Diễn giải: một nhóm tương đối nhỏ đóng góp phần đáng kể lượng nội dung.",
    finding2Limit:
      "Giới hạn: chỉ số này chưa giải thích được nguyên nhân nhóm đó đăng nhiều hơn.",
    finding3Title: "Hoạt động đăng bài thay đổi theo thời gian",
    questionsTitle: "Các câu hỏi kinh doanh cần phân tích",
    questionsSubtitle:
      "Quy trình phân tích thực tế bắt đầu từ câu hỏi, bằng chứng và bước tiếp theo.",
    question: "Câu hỏi kinh doanh",
    evidence: "Bằng chứng hiện có",
    nextStep: "Phân tích tiếp theo",
    q1: "Bao nhiêu người dùng có đóng góp nội dung?",
    e1: "480 trong số 600 người dùng đã đăng ít nhất một bài.",
    n1: "So sánh người dùng mới, quay lại và không hoạt động theo thời gian.",
    q2: "Hoạt động tạo nội dung tập trung đến mức nào?",
    e2: "Nhóm 10% người tạo nhiều nhất đóng góp 38,67% số bài.",
    n2: "Tính các phân vị người tạo nội dung và so sánh nhóm tần suất đăng bài.",
    q3: "Thời điểm nào có hoạt động đăng bài cao nhất?",
    n3: "So sánh các tháng đầy đủ và kiểm tra tính mùa vụ trước khi kết luận.",
    q4: "Điều gì xảy ra khi bản nháp chuyển thành bài xuất bản?",
    e4: "Tỷ trọng trạng thái hiện tại là 70% đã xuất bản, 20% bản nháp và 10% lưu trữ.",
    n4: "Dùng thời điểm thay đổi trạng thái để đo tỷ lệ xuất bản và thời gian chờ.",
    qualityTitle: "Chất lượng dữ liệu và phương pháp",
    qualitySubtitle:
      "Xác định những gì dữ liệu hỗ trợ và không hỗ trợ trước khi đề xuất.",
    source: "Nguồn dữ liệu",
    sourceValue: "Bộ dữ liệu phân tích mô phỏng được tạo tự động",
    scope: "Phạm vi dữ liệu",
    completeness: "Khoảng thời gian",
    caveat: "Lưu ý quan trọng",
    caveatValue:
      "Tháng mới nhất có thể chưa hoàn tất. Khi so sánh theo tháng, chỉ nên dùng các tháng đã hoàn tất.",
    limitation: "Giới hạn phân tích",
    limitationValue:
      "Tỷ trọng trạng thái hiện tại không cho biết quá trình chuyển từ bản nháp sang xuất bản nếu thiếu thời điểm thay đổi trạng thái.",
    workflow: "Quy trình của Data Analyst",
    step1: "Xác định câu hỏi kinh doanh",
    step2: "Kiểm tra dữ liệu và phạm vi",
    step3: "Khám phá xu hướng và so sánh nhóm",
    step4: "Giải thích phát hiện và giới hạn",
    step5: "Đề xuất phân tích tiếp theo",
    footer:
      "Dự án portfolio · Dữ liệu mô phỏng · Phát hiện mang tính mô tả, không khẳng định quan hệ nhân quả",
    themeLight: "Giao diện sáng",
    themeDark: "Giao diện tối",
    language: "Ngôn ngữ",
    periodLabel: "Khoảng thời gian",
    noData: "Không có dữ liệu theo tháng.",
  },
};

const statusColors = ["#16a34a", "#f59e0b", "#64748b"];

export default function Home() {
  const [language, setLanguage] = useState<Language>("en");
  const [theme, setTheme] = useState<Theme>("light");
  const [period, setPeriod] = useState<Period>("all");

  const t = translations[language];
  const isDark = theme === "dark";

  const filteredMonthlyPosts = useMemo(() => {
    if (period === "all") return monthlyPosts;
    return monthlyPosts.slice(-Number(period));
  }, [period]);

  const selectedPeriodTotal = filteredMonthlyPosts.reduce(
    (sum, row) => sum + Number(row.posts || 0),
    0
  );

  const formatNumber = (value: number) =>
    new Intl.NumberFormat(language === "en" ? "en-US" : "vi-VN").format(value);

  const formatPercent = (
    value: number,
    maximumFractionDigits = 1
  ) =>
    new Intl.NumberFormat(language === "en" ? "en-US" : "vi-VN", {
      maximumFractionDigits,
    }).format(value) + "%";

  const totalUsers = progress.stats.analyticsUsers;
  const participationRate = progress.stats.postingRate;
  const usersWhoPosted = Math.round(
    (totalUsers * participationRate) / 100
  );

  const statusData = [
    {
      name: t.published,
      value: progress.stats.statusShares.published,
    },
    {
      name: t.draft,
      value: progress.stats.statusShares.draft,
    },
    {
      name: t.archived,
      value: progress.stats.statusShares.archived,
    },
  ];


  const monthlyData = progress.monthlyPosts;
  const latestMonth = monthlyData[monthlyData.length - 1];

  // Tháng cuối cùng là tháng chưa hoàn tất nên không dùng để tìm đỉnh.
  const completedMonthlyData = latestMonth
    ? monthlyData.filter((row) => row.month < latestMonth.month)
    : monthlyData;

  const peakMonth = completedMonthlyData.length
    ? completedMonthlyData.reduce((best, row) =>
        row.posts > best.posts ? row : best
      )
    : undefined;

  const formatMonthLabel = (month: string) =>
    new Intl.DateTimeFormat(
      language === "en" ? "en-US" : "vi-VN",
      {
        month: "long",
        year: "numeric",
        timeZone: "UTC",
      }
    ).format(new Date(`${month}-01T00:00:00Z`));

  const datasetScope =
    language === "en"
      ? `${formatNumber(totalUsers)} users · ${formatNumber(progress.stats.analyticsPosts)} posts`
      : `${formatNumber(totalUsers)} người dùng · ${formatNumber(progress.stats.analyticsPosts)} bài đăng`;

  const coverageRange = monthlyData.length
    ? language === "en"
      ? `${formatMonthLabel(monthlyData[0].month)}–${formatMonthLabel(monthlyData[monthlyData.length - 1].month)}`
      : `Tháng ${Number(monthlyData[0].month.slice(5, 7))}/${monthlyData[0].month.slice(0, 4)}–tháng ${Number(monthlyData[monthlyData.length - 1].month.slice(5, 7))}/${monthlyData[monthlyData.length - 1].month.slice(0, 4)}`
    : "—";

  const primaryText = isDark ? "text-slate-100" : "text-slate-900";
  const secondaryText = isDark ? "text-slate-400" : "text-slate-500";
  const pageBackground = isDark
    ? "bg-[#080d19] text-slate-100"
    : "bg-slate-50 text-slate-900";

  const navItems = [
    { label: t.overview, href: "#overview", icon: LayoutDashboard },
    { label: t.storytelling, href: "#storytelling", icon: TrendingUp },
    { label: t.questions, href: "#questions", icon: Target },
    { label: t.quality, href: "#quality", icon: ShieldCheck },
  ];

  const kpis = [
    {
      label: t.users,
      value: formatNumber(totalUsers),
      note: t.ofUsers,
      icon: Users,
      accent: "text-blue-500",
      iconBg: isDark ? "bg-blue-500/10" : "bg-blue-50",
    },
    {
      label: t.activeUsers,
      value: formatNumber(usersWhoPosted),
      note: t.havePosted,
      icon: Activity,
      accent: "text-emerald-500",
      iconBg: isDark ? "bg-emerald-500/10" : "bg-emerald-50",
    },
    {
      label: t.participation,
      value: formatPercent(participationRate),
      note: t.engagement,
      icon: Target,
      accent: "text-violet-500",
      iconBg: isDark ? "bg-violet-500/10" : "bg-violet-50",
    },
    {
      label: t.totalPosts,
      value: formatNumber(selectedPeriodTotal),
      note: t.periodPosts,
      icon: FileText,
      accent: "text-amber-500",
      iconBg: isDark ? "bg-amber-500/10" : "bg-amber-50",
    },
  ];

  const findings = [
    {
      number: "01",
      title: t.finding1Title,
      description:
        language === "en"
          ? `${formatNumber(usersWhoPosted)} of ${formatNumber(totalUsers)} users have created at least one post, giving the dataset a ${formatPercent(participationRate)} posting-user rate.`
          : `${formatNumber(usersWhoPosted)} trong số ${formatNumber(totalUsers)} người dùng đã tạo ít nhất một bài đăng, tương đương tỷ lệ ${formatPercent(participationRate)}.`,
      meaning: t.finding1Meaning,
      limitation: t.finding1Limit,
      icon: Users,
      color: "text-blue-500",
    },
    {
      number: "02",
      title: t.finding2Title,
      description:
        language === "en"
          ? `The top 10% of creators account for ${formatPercent(progress.stats.topCreatorShare, 2)} of all posts in the dataset.`
          : `Nhóm 10% người tạo nội dung nhiều nhất đóng góp ${formatPercent(progress.stats.topCreatorShare, 2)} tổng số bài đăng.`,
      meaning: t.finding2Meaning,
      limitation: t.finding2Limit,
      icon: Target,
      color: "text-violet-500",
    },
    {
      number: "03",
      title: t.finding3Title,
      description: peakMonth
        ? language === "en"
          ? `${formatMonthLabel(peakMonth.month)} recorded ${formatNumber(peakMonth.posts)} posts, the highest monthly count among the completed months shown.`
          : `${formatMonthLabel(peakMonth.month)} ghi nhận ${formatNumber(peakMonth.posts)} bài đăng, cao nhất trong các tháng đã hoàn tất.`
        : language === "en"
          ? "No completed monthly data is available yet."
          : "Chưa có dữ liệu tháng đã hoàn tất.",
      meaning: peakMonth
        ? language === "en"
          ? `${formatMonthLabel(peakMonth.month)} is a useful period for further investigation of content activity.`
          : `${formatMonthLabel(peakMonth.month)} là giai đoạn phù hợp để tìm hiểu sâu hơn về hoạt động nội dung.`
        : language === "en"
          ? "Review the monthly data after a complete month becomes available."
          : "Hãy xem xét dữ liệu khi có tháng đã hoàn tất.",
      limitation: latestMonth
        ? language === "en"
          ? `${formatMonthLabel(latestMonth.month)} may be incomplete and should not be compared as a full month.`
          : `${formatMonthLabel(latestMonth.month)} có thể chưa hoàn tất, vì vậy không nên so sánh như một tháng đầy đủ.`
        : language === "en"
          ? "Check the completeness of the monthly data before comparing periods."
          : "Cần kiểm tra độ đầy đủ của dữ liệu tháng trước khi so sánh.",
      icon: TrendingUp,
      color: "text-emerald-500",
    },
  ];

  const businessQuestions = [
    {
      number: "01",
      q: t.q1,
      evidence:
        language === "en"
          ? `${formatNumber(usersWhoPosted)} of ${formatNumber(totalUsers)} users have posted at least once.`
          : `${formatNumber(usersWhoPosted)} trong số ${formatNumber(totalUsers)} người dùng đã đăng ít nhất một bài.`,
      next: t.n1,
    },
    {
      number: "02",
      q: t.q2,
      evidence:
        language === "en"
          ? `The top 10% of creators produce ${formatPercent(progress.stats.topCreatorShare, 2)} of posts.`
          : `Nhóm 10% người tạo nhiều nhất đóng góp ${formatPercent(progress.stats.topCreatorShare, 2)} số bài đăng.`,
      next: t.n2,
    },
    {
      number: "03",
      q: t.q3,
      evidence: peakMonth
        ? language === "en"
          ? `${formatMonthLabel(peakMonth.month)} has ${formatNumber(peakMonth.posts)} posts, the highest among completed months.`
          : `${formatMonthLabel(peakMonth.month)} có ${formatNumber(peakMonth.posts)} bài đăng, cao nhất trong các tháng đã hoàn tất.`
        : language === "en"
          ? "No completed monthly data is available yet."
          : "Chưa có dữ liệu tháng đã hoàn tất.",
      next: t.n3,
    },
    {
      number: "04",
      q: t.q4,
      evidence:
        language === "en"
          ? `Current status shares are ${formatPercent(progress.stats.statusShares.published, 0)} published, ${formatPercent(progress.stats.statusShares.draft, 0)} draft, and ${formatPercent(progress.stats.statusShares.archived, 0)} archived.`
          : `Tỷ trọng trạng thái hiện tại là ${formatPercent(progress.stats.statusShares.published, 0)} đã xuất bản, ${formatPercent(progress.stats.statusShares.draft, 0)} bản nháp và ${formatPercent(progress.stats.statusShares.archived, 0)} đã lưu trữ.`,
      next: t.n4,
    },
  ];

  const workflowSteps = [t.step1, t.step2, t.step3, t.step4, t.step5];

  return (
    <main className={`min-h-screen ${pageBackground} transition-colors duration-200`}>
      <div className="flex min-h-screen">
        <aside
          className={`hidden w-64 shrink-0 border-r px-5 py-7 lg:flex lg:flex-col ${
            isDark ? "border-slate-800 bg-slate-950" : "border-slate-200 bg-white"
          }`}
        >
          <div className="mb-10 flex items-center gap-3">
            <div className="flex h-11 w-11 items-center justify-center rounded-2xl bg-blue-600 text-white shadow-lg shadow-blue-600/20">
              <BarChart3 size={23} />
            </div>
            <div>
              <p className={`font-bold tracking-tight ${primaryText}`}>InsightLab</p>
              <p className={`text-xs ${secondaryText}`}>Analytics Studio</p>
            </div>
          </div>

          <p className={`mb-3 px-3 text-[10px] font-bold tracking-[0.18em] ${secondaryText}`}>
            {t.workspace}
          </p>

          <nav className="space-y-1">
            {navItems.map((item, index) => {
              const Icon = item.icon;
              return (
                <a
                  key={item.href}
                  href={item.href}
                  className={`flex items-center gap-3 rounded-xl px-3 py-3 text-sm transition ${
                    index === 0
                      ? "bg-blue-600 font-semibold text-white shadow-md shadow-blue-600/15"
                      : isDark
                        ? "text-slate-400 hover:bg-slate-900 hover:text-slate-100"
                        : "text-slate-600 hover:bg-slate-100 hover:text-slate-900"
                  }`}
                >
                  <Icon size={18} />
                  <span>{item.label}</span>
                  {index === 0 && <ChevronRight className="ml-auto" size={15} />}
                </a>
              );
            })}
          </nav>

          <div className="mt-auto">
            <div
              className={`rounded-2xl border p-4 ${
                isDark ? "border-slate-800 bg-slate-900" : "border-slate-200 bg-slate-50"
              }`}
            >
              <div className="mb-3 flex items-center gap-2">
                <Database size={17} className="text-blue-500" />
                <span className={`text-sm font-semibold ${primaryText}`}>{t.sample}</span>
              </div>
              <p className={`text-xs leading-5 ${secondaryText}`}>
                {datasetScope}
              </p>
              <div className="mt-3 flex items-center gap-2 text-xs text-emerald-500">
                <CheckCircle2 size={14} />
                <span>{language === "en" ? "Ready for exploration" : "Sẵn sàng phân tích"}</span>
              </div>
            </div>
            <p className={`mt-5 text-xs ${secondaryText}`}>Portfolio v1.0</p>
          </div>
        </aside>

        <div className="min-w-0 flex-1">
          <header
            className={`sticky top-0 z-20 border-b backdrop-blur-xl ${
              isDark
                ? "border-slate-800 bg-[#080d19]/90"
                : "border-slate-200 bg-white/90"
            }`}
          >
            <div className="mx-auto flex max-w-[1600px] flex-wrap items-center justify-between gap-3 px-4 py-4 sm:px-6 xl:px-9">
              <div className="flex items-center gap-3">
                <div className="flex h-10 w-10 items-center justify-center rounded-xl bg-blue-600 text-white lg:hidden">
                  <BarChart3 size={21} />
                </div>
                <div>
                  <p className={`text-sm font-semibold ${primaryText}`}>InsightLab</p>
                  <p className={`text-xs ${secondaryText}`}>{t.portfolio}</p>
                </div>
              </div>

              <div className="flex flex-wrap items-center gap-2">
                <label className="sr-only" htmlFor="period-filter">
                  {t.periodLabel}
                </label>
                <select
                  id="period-filter"
                  value={period}
                  onChange={(event) => setPeriod(event.target.value as Period)}
                  className={`rounded-xl border px-3 py-2.5 text-sm outline-none focus:border-blue-500 ${
                    isDark
                      ? "border-slate-700 bg-slate-900 text-slate-200"
                      : "border-slate-200 bg-white text-slate-700"
                  }`}
                >
                  <option value="all">{t.allTime}</option>
                  <option value="6">{t.last6}</option>
                  <option value="3">{t.last3}</option>
                </select>

                <button
                  type="button"
                  onClick={() => setLanguage((current) => current === "en" ? "vi" : "en")}
                  aria-label={t.language}
                  className={`flex items-center gap-2 rounded-xl border px-3 py-2.5 text-sm font-medium transition ${
                    isDark
                      ? "border-slate-700 hover:bg-slate-800"
                      : "border-slate-200 hover:bg-slate-100"
                  }`}
                >
                  <Globe2 size={16} />
                  {language === "en" ? "EN / VI" : "VI / EN"}
                </button>

                <button
                  type="button"
                  onClick={() => setTheme((current) => current === "light" ? "dark" : "light")}
                  aria-label={isDark ? t.themeLight : t.themeDark}
                  className={`flex items-center gap-2 rounded-xl border px-3 py-2.5 text-sm font-medium transition ${
                    isDark
                      ? "border-slate-700 hover:bg-slate-800"
                      : "border-slate-200 hover:bg-slate-100"
                  }`}
                >
                  {isDark ? <Sun size={16} /> : <Moon size={16} />}
                  <span className="hidden sm:inline">
                    {isDark ? t.themeLight : t.themeDark}
                  </span>
                </button>
              </div>
            </div>
          </header>

          <div className="mx-auto max-w-[1600px] space-y-8 px-4 py-7 sm:px-6 sm:py-9 xl:px-9">
            <section id="overview">
              <div className="mb-7 flex flex-col justify-between gap-4 md:flex-row md:items-end">
                <div>
                  <div className="mb-3 flex flex-wrap items-center gap-2">
                    <span className="rounded-full bg-blue-500/10 px-3 py-1 text-[11px] font-bold tracking-wide text-blue-500">
                      {t.portfolio}
                    </span>
                    <span
                      className={`rounded-full border px-3 py-1 text-[11px] ${
                        isDark
                          ? "border-slate-700 text-slate-400"
                          : "border-slate-200 text-slate-500"
                      }`}
                    >
                      {t.sample}
                    </span>
                  </div>
                  <h1 className={`text-3xl font-bold tracking-tight sm:text-4xl ${primaryText}`}>
                    {t.title}
                  </h1>
                  <p className={`mt-3 max-w-3xl text-sm leading-6 sm:text-base ${secondaryText}`}>
                    {t.subtitle}
                  </p>
                </div>

                <div
                  className={`flex items-center gap-3 rounded-xl border px-4 py-3 ${
                    isDark ? "border-slate-800 bg-slate-900" : "border-slate-200 bg-white"
                  }`}
                >
                  <div className={`flex h-9 w-9 items-center justify-center rounded-lg ${
                    isDark ? "bg-slate-800" : "bg-slate-100"
                  }`}>
                    <Activity size={18} className="text-blue-500" />
                  </div>
                  <div>
                    <p className={`text-xs ${secondaryText}`}>{t.lastUpdated}</p>
                    <p className={`text-sm font-semibold ${primaryText}`}>
                      {period === "all" ? t.allTime : period === "6" ? t.last6 : t.last3}
                    </p>
                  </div>
                </div>
              </div>

              <div className="grid gap-4 sm:grid-cols-2 2xl:grid-cols-4">
                {kpis.map((kpi) => {
                  const Icon = kpi.icon;
                  return (
                    <article
                      key={kpi.label}
                      className={`rounded-2xl border p-5 shadow-sm transition hover:-translate-y-0.5 hover:shadow-md ${
                        isDark ? "border-slate-800 bg-slate-900" : "border-slate-200 bg-white"
                      }`}
                    >
                      <div className="flex items-start justify-between gap-3">
                        <div>
                          <p className={`text-sm font-medium ${secondaryText}`}>{kpi.label}</p>
                          <p className={`mt-3 text-3xl font-bold tracking-tight ${primaryText}`}>
                            {kpi.value}
                          </p>
                        </div>
                        <div className={`flex h-11 w-11 items-center justify-center rounded-xl ${kpi.iconBg} ${kpi.accent}`}>
                          <Icon size={21} />
                        </div>
                      </div>
                      <p className={`mt-4 text-xs leading-5 ${secondaryText}`}>{kpi.note}</p>
                    </article>
                  );
                })}
              </div>
            </section>

            <section className="grid gap-5 xl:grid-cols-[minmax(0,1.7fr)_minmax(320px,0.9fr)]">
              <article
                className={`rounded-2xl border p-5 shadow-sm sm:p-6 ${
                  isDark ? "border-slate-800 bg-slate-900" : "border-slate-200 bg-white"
                }`}
              >
                <div className="mb-6 flex flex-wrap items-start justify-between gap-3">
                  <div>
                    <h2 className={`text-lg font-bold ${primaryText}`}>{t.monthlyTitle}</h2>
                    <p className={`mt-1 text-sm ${secondaryText}`}>{t.monthlySubtitle}</p>
                  </div>
                  <div className="flex items-center gap-2 rounded-lg bg-blue-500/10 px-3 py-2 text-xs font-semibold text-blue-500">
                    <BarChart3 size={15} />
                    {t.posts}
                  </div>
                </div>

                <div className="h-[300px] w-full">
                  {filteredMonthlyPosts.length > 0 ? (
                    <ResponsiveContainer width="100%" height="100%">
                      <BarChart data={filteredMonthlyPosts} margin={{ top: 8, right: 8, left: -18, bottom: 4 }}>
                        <CartesianGrid
                          strokeDasharray="3 3"
                          vertical={false}
                          stroke={isDark ? "#263244" : "#e2e8f0"}
                        />
                        <XAxis
                          dataKey="month"
                          axisLine={false}
                          tickLine={false}
                          tick={{ fill: isDark ? "#94a3b8" : "#64748b", fontSize: 11 }}
                          dy={8}
                        />
                        <YAxis
                          axisLine={false}
                          tickLine={false}
                          tick={{ fill: isDark ? "#94a3b8" : "#64748b", fontSize: 11 }}
                          tickFormatter={(value) => formatNumber(Number(value))}
                        />
                        <Tooltip
                          cursor={{ fill: isDark ? "#1e293b" : "#f1f5f9" }}
                          contentStyle={{
                            backgroundColor: isDark ? "#0f172a" : "#ffffff",
                            border: `1px solid ${isDark ? "#334155" : "#e2e8f0"}`,
                            borderRadius: 12,
                            color: isDark ? "#f8fafc" : "#0f172a",
                          }}
                          labelStyle={{
                            color: isDark ? "#f8fafc" : "#0f172a",
                            fontWeight: 600,
                            marginBottom: 4,
                          }}
                          formatter={(value) => [formatNumber(Number(value)), t.posts]}
                        />
                        <Bar
                          dataKey="posts"
                          name={t.posts}
                          fill="#3b82f6"
                          radius={[6, 6, 0, 0]}
                          maxBarSize={44}
                        />
                      </BarChart>
                    </ResponsiveContainer>
                  ) : (
                    <div className={`flex h-full items-center justify-center text-sm ${secondaryText}`}>
                      {t.noData}
                    </div>
                  )}
                </div>

                <div
                  className={`mt-4 flex flex-wrap items-center justify-between gap-2 border-t pt-4 ${
                    isDark ? "border-slate-800" : "border-slate-100"
                  }`}
                >
                  <p className={`text-xs ${secondaryText}`}>{t.selectedTotal}</p>
                  <p className={`text-sm font-bold ${primaryText}`}>
                    {formatNumber(selectedPeriodTotal)} {t.posts.toLowerCase()}
                  </p>
                </div>
              </article>

              <article
                className={`rounded-2xl border p-5 shadow-sm sm:p-6 ${
                  isDark ? "border-slate-800 bg-slate-900" : "border-slate-200 bg-white"
                }`}
              >
                <div className="mb-3">
                  <h2 className={`text-lg font-bold ${primaryText}`}>{t.statusTitle}</h2>
                  <p className={`mt-1 text-sm ${secondaryText}`}>{t.statusSubtitle}</p>
                </div>

                <div className="relative h-[230px]">
                  <ResponsiveContainer width="100%" height="100%">
                    <PieChart>
                      <Pie
                        data={statusData}
                        dataKey="value"
                        nameKey="name"
                        cx="50%"
                        cy="50%"
                        innerRadius={62}
                        outerRadius={88}
                        paddingAngle={4}
                        stroke="none"
                      >
                        {statusData.map((entry, index) => (
                          <Cell key={entry.name} fill={statusColors[index]} />
                        ))}
                      </Pie>
                      <Tooltip
                        formatter={(value) => [formatPercent(Number(value)), language === "en" ? "Share" : "Tỷ trọng"]}
                        contentStyle={{
                          backgroundColor: isDark ? "#0f172a" : "#ffffff",
                          border: `1px solid ${isDark ? "#334155" : "#e2e8f0"}`,
                          borderRadius: 12,
                          color: isDark ? "#f8fafc" : "#0f172a",
                        }}
                      />
                    </PieChart>
                  </ResponsiveContainer>
                  <div className="pointer-events-none absolute inset-0 flex flex-col items-center justify-center">
                    <span className={`text-3xl font-bold ${primaryText}`}>100%</span>
                    <span className={`mt-1 text-xs ${secondaryText}`}>
                      {language === "en" ? "All statuses" : "Tất cả trạng thái"}
                    </span>
                  </div>
                </div>

                <div className="space-y-3">
                  {statusData.map((item, index) => (
                    <div key={item.name} className="flex items-center justify-between gap-3">
                      <div className="flex items-center gap-2.5">
                        <span
                          className="h-2.5 w-2.5 rounded-full"
                          style={{ backgroundColor: statusColors[index] }}
                        />
                        <span className={`text-sm ${secondaryText}`}>{item.name}</span>
                      </div>
                      <span className={`text-sm font-semibold ${primaryText}`}>
                        {formatPercent(item.value)}
                      </span>
                    </div>
                  ))}
                </div>
              </article>
            </section>

            <section id="storytelling">
              <div className="mb-5">
                <div className="mb-2 flex items-center gap-2 text-blue-500">
                  <TrendingUp size={18} />
                  <span className="text-xs font-bold tracking-[0.16em]">
                    {t.storytelling.toUpperCase()}
                  </span>
                </div>
                <h2 className={`text-2xl font-bold tracking-tight ${primaryText}`}>
                  {t.storytellingTitle}
                </h2>
                <p className={`mt-2 text-sm ${secondaryText}`}>{t.storytellingSubtitle}</p>
              </div>

              <div className="grid gap-4 xl:grid-cols-3">
                {findings.map((finding) => {
                  const Icon = finding.icon;
                  return (
                    <article
                      key={finding.number}
                      className={`rounded-2xl border p-5 sm:p-6 ${
                        isDark ? "border-slate-800 bg-slate-900" : "border-slate-200 bg-white"
                      }`}
                    >
                      <div className="mb-5 flex items-center justify-between">
                        <span className={`text-xs font-bold tracking-[0.16em] ${secondaryText}`}>
                          FINDING {finding.number}
                        </span>
                        <div className={`flex h-10 w-10 items-center justify-center rounded-xl ${
                          isDark ? "bg-slate-800" : "bg-slate-100"
                        } ${finding.color}`}>
                          <Icon size={20} />
                        </div>
                      </div>
                      <h3 className={`text-base font-bold leading-6 ${primaryText}`}>
                        {finding.title}
                      </h3>
                      <p className={`mt-3 text-sm leading-6 ${secondaryText}`}>
                        {finding.description}
                      </p>

                      <div className={`mt-5 rounded-xl p-3.5 ${
                        isDark ? "bg-slate-800/70" : "bg-slate-50"
                      }`}>
                        <p className={`text-xs font-semibold ${primaryText}`}>
                          {language === "en" ? "Interpretation" : "Diễn giải"}
                        </p>
                        <p className={`mt-1.5 text-xs leading-5 ${secondaryText}`}>
                          {finding.meaning}
                        </p>
                      </div>

                      <div className="mt-4 flex items-start gap-2">
                        <CircleHelp className="mt-0.5 shrink-0 text-amber-500" size={15} />
                        <p className={`text-xs leading-5 ${secondaryText}`}>
                          {finding.limitation}
                        </p>
                      </div>
                    </article>
                  );
                })}
              </div>
            </section>

            <section id="questions">
              <div className="mb-5">
                <div className="mb-2 flex items-center gap-2 text-violet-500">
                  <Target size={18} />
                  <span className="text-xs font-bold tracking-[0.16em]">
                    {t.questions.toUpperCase()}
                  </span>
                </div>
                <h2 className={`text-2xl font-bold tracking-tight ${primaryText}`}>
                  {t.questionsTitle}
                </h2>
                <p className={`mt-2 text-sm ${secondaryText}`}>{t.questionsSubtitle}</p>
              </div>

              <div className={`overflow-hidden rounded-2xl border ${
                isDark ? "border-slate-800 bg-slate-900" : "border-slate-200 bg-white"
              }`}>
                <div className={`hidden grid-cols-[minmax(0,1fr)_minmax(0,1fr)_minmax(0,1fr)] gap-5 border-b px-6 py-4 md:grid ${
                  isDark ? "border-slate-800 bg-slate-950/60" : "border-slate-100 bg-slate-50"
                }`}>
                  <p className={`text-xs font-bold uppercase tracking-wide ${secondaryText}`}>{t.question}</p>
                  <p className={`text-xs font-bold uppercase tracking-wide ${secondaryText}`}>{t.evidence}</p>
                  <p className={`text-xs font-bold uppercase tracking-wide ${secondaryText}`}>{t.nextStep}</p>
                </div>

                {businessQuestions.map((item) => (
                  <div
                    key={item.number}
                    className={`grid gap-3 border-b p-5 last:border-b-0 md:grid-cols-[minmax(0,1fr)_minmax(0,1fr)_minmax(0,1fr)] md:gap-5 md:px-6 ${
                      isDark ? "border-slate-800" : "border-slate-100"
                    }`}
                  >
                    <div className="flex items-start gap-3">
                      <span className="flex h-8 w-8 shrink-0 items-center justify-center rounded-lg bg-blue-500/10 text-xs font-bold text-blue-500">
                        {item.number}
                      </span>
                      <div>
                        <p className={`mb-1 text-[10px] font-bold uppercase tracking-wide md:hidden ${secondaryText}`}>
                          {t.question}
                        </p>
                        <p className={`text-sm font-semibold leading-6 ${primaryText}`}>{item.q}</p>
                      </div>
                    </div>

                    <div>
                      <p className={`mb-1 text-[10px] font-bold uppercase tracking-wide md:hidden ${secondaryText}`}>
                        {t.evidence}
                      </p>
                      <p className={`text-sm leading-6 ${secondaryText}`}>{item.evidence}</p>
                    </div>

                    <div>
                      <p className={`mb-1 text-[10px] font-bold uppercase tracking-wide md:hidden ${secondaryText}`}>
                        {t.nextStep}
                      </p>
                      <div className="flex items-start gap-2">
                        <ArrowUpRight className="mt-0.5 shrink-0 text-emerald-500" size={16} />
                        <p className={`text-sm leading-6 ${secondaryText}`}>{item.next}</p>
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            </section>

            <section id="quality">
              <div className="mb-5">
                <div className="mb-2 flex items-center gap-2 text-emerald-500">
                  <ShieldCheck size={18} />
                  <span className="text-xs font-bold tracking-[0.16em]">
                    {t.quality.toUpperCase()}
                  </span>
                </div>
                <h2 className={`text-2xl font-bold tracking-tight ${primaryText}`}>
                  {t.qualityTitle}
                </h2>
                <p className={`mt-2 text-sm ${secondaryText}`}>{t.qualitySubtitle}</p>
              </div>

              <div className="grid gap-5 xl:grid-cols-[minmax(0,1.15fr)_minmax(0,0.85fr)]">
                <article className={`rounded-2xl border p-5 sm:p-6 ${
                  isDark ? "border-slate-800 bg-slate-900" : "border-slate-200 bg-white"
                }`}>
                  <div className="space-y-5">
                    {[
                      { label: t.source, value: t.sourceValue, icon: Database },
                      { label: t.scope, value: datasetScope, icon: Users },
                      { label: t.completeness, value: coverageRange, icon: Activity },
                    ].map((item) => {
                      const Icon = item.icon;
                      return (
                        <div key={item.label} className="flex items-start gap-3">
                          <div className={`flex h-10 w-10 shrink-0 items-center justify-center rounded-xl ${
                            isDark ? "bg-slate-800" : "bg-slate-100"
                          }`}>
                            <Icon size={18} className="text-blue-500" />
                          </div>
                          <div>
                            <p className={`text-xs ${secondaryText}`}>{item.label}</p>
                            <p className={`mt-1 text-sm font-semibold leading-6 ${primaryText}`}>
                              {item.value}
                            </p>
                          </div>
                        </div>
                      );
                    })}
                  </div>

                  <div className={`mt-6 rounded-xl border p-4 ${
                    isDark
                      ? "border-amber-500/20 bg-amber-500/5"
                      : "border-amber-200 bg-amber-50/70"
                  }`}>
                    <div className="flex items-center gap-2 text-amber-500">
                      <CircleHelp size={17} />
                      <p className="text-sm font-bold">{t.caveat}</p>
                    </div>
                    <p className={`mt-2 text-sm leading-6 ${secondaryText}`}>{t.caveatValue}</p>
                  </div>

                  <div className={`mt-3 rounded-xl border p-4 ${
                    isDark
                      ? "border-slate-700 bg-slate-800/50"
                      : "border-slate-200 bg-slate-50"
                  }`}>
                    <p className={`text-sm font-bold ${primaryText}`}>{t.limitation}</p>
                    <p className={`mt-2 text-sm leading-6 ${secondaryText}`}>{t.limitationValue}</p>
                  </div>
                </article>

                <article className={`rounded-2xl border p-5 sm:p-6 ${
                  isDark ? "border-slate-800 bg-slate-900" : "border-slate-200 bg-white"
                }`}>
                  <h3 className={`text-lg font-bold ${primaryText}`}>{t.workflow}</h3>
                  <p className={`mt-1 text-sm ${secondaryText}`}>
                    {language === "en"
                      ? "A repeatable process for an internship or fresher project."
                      : "Một quy trình có thể áp dụng cho dự án thực tập hoặc Fresher."}
                  </p>

                  <div className="mt-6 space-y-0">
                    {workflowSteps.map((step, index) => (
                      <div key={step} className="flex gap-4">
                        <div className="flex flex-col items-center">
                          <div className={`flex h-9 w-9 shrink-0 items-center justify-center rounded-full text-sm font-bold ${
                            index === workflowSteps.length - 1
                              ? "bg-emerald-500 text-white"
                              : "bg-blue-600 text-white"
                          }`}>
                            {index === workflowSteps.length - 1 ? (
                              <CheckCircle2 size={18} />
                            ) : (
                              index + 1
                            )}
                          </div>
                          {index < workflowSteps.length - 1 && (
                            <div className={`my-1 min-h-7 w-px flex-1 ${
                              isDark ? "bg-slate-700" : "bg-slate-200"
                            }`} />
                          )}
                        </div>
                        <div className="pb-6 pt-1">
                          <p className={`text-sm font-medium leading-6 ${primaryText}`}>{step}</p>
                        </div>
                      </div>
                    ))}
                  </div>
                </article>
              </div>
            </section>

            <footer className={`border-t pt-5 ${
              isDark ? "border-slate-800" : "border-slate-200"
            }`}>
              <div className="flex flex-col justify-between gap-2 pb-3 sm:flex-row sm:items-center">
                <p className={`text-xs leading-5 ${secondaryText}`}>{t.footer}</p>
                <a
                  href="#overview"
                  className="inline-flex items-center gap-1 text-xs font-semibold text-blue-500 hover:text-blue-400"
                >
                  {t.overview}
                  <ArrowDownRight size={14} />
                </a>
              </div>
            </footer>
          </div>
        </div>
      </div>
    </main>
  );
}
