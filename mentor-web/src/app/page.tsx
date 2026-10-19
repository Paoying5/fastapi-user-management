"use client";

import {
  ArrowUpRight,
  CheckCircle2,
  Circle,
  Code2,
  Database,
  GitBranch,
  Sparkles,
  TestTube2,
  TrendingUp,
} from "lucide-react";

import { motion } from "motion/react";

const stats = [
  {
    value: "79",
    label: "Tests Passed",
    description: "Full regression",
    icon: TestTube2,
  },
  {
    value: "600",
    label: "Analytics Users",
    description: "Synthetic dataset",
    icon: Database,
  },
  {
    value: "2,250",
    label: "Analytics Posts",
    description: "Ready for analysis",
    icon: Code2,
  },
  {
    value: "80%",
    label: "Posting Rate",
    description: "Exploratory KPI",
    icon: TrendingUp,
  },
];

const roadmap = [
  {
    title: "FastAPI Foundations",
    status: "completed",
  },
  {
    title: "Architecture & Database",
    status: "completed",
  },
  {
    title: "Testing & E2E",
    status: "completed",
  },
  {
    title: "SQL Analytics",
    status: "current",
  },
  {
    title: "Pandas & EDA",
    status: "next",
  },
  {
    title: "Visualization",
    status: "planned",
  },
  {
    title: "Analytics Dashboard",
    status: "planned",
  },
];

const weekHighlights = [
  "Completed User and Post lifecycle",
  "Verified authentication lifecycle",
  "Applied PostgreSQL lifecycle migration",
  "Reached 79 passing automated tests",
  "Created 600-user analytics dataset",
  "Analyzed 2,250 synthetic posts",
  "Completed SQL KPI analysis",
  "Practiced business questions and window functions",
];

const container = {
  hidden: {},
  show: {
    transition: {
      staggerChildren: 0.08,
    },
  },
};

const item = {
  hidden: {
    opacity: 0,
    y: 24,
  },
  show: {
    opacity: 1,
    y: 0,
    transition: {
      duration: 0.6,
    },
  },
};

export default function Home() {
  return (
    <main className="min-h-screen overflow-hidden bg-[#f8fafc] text-slate-950">
      {/* Background */}
      <div className="pointer-events-none fixed inset-0 overflow-hidden">
        <motion.div
          animate={{
            x: [0, 30, 0],
            y: [0, -20, 0],
          }}
          transition={{
            duration: 12,
            repeat: Infinity,
            ease: "easeInOut",
          }}
          className="absolute left-[-8rem] top-[-8rem] h-[28rem] w-[28rem] rounded-full bg-indigo-200/35 blur-[110px]"
        />

        <motion.div
          animate={{
            x: [0, -30, 0],
            y: [0, 30, 0],
          }}
          transition={{
            duration: 15,
            repeat: Infinity,
            ease: "easeInOut",
          }}
          className="absolute right-[-10rem] top-[20rem] h-[32rem] w-[32rem] rounded-full bg-violet-200/30 blur-[120px]"
        />

        <div className="absolute inset-0 bg-[linear-gradient(to_right,#0f172a0a_1px,transparent_1px),linear-gradient(to_bottom,#0f172a0a_1px,transparent_1px)] bg-[size:42px_42px] [mask-image:linear-gradient(to_bottom,black,transparent_80%)]" />
      </div>

      {/* Navbar */}
      <header className="sticky top-0 z-50 border-b border-white/60 bg-white/70 backdrop-blur-xl">
        <div className="mx-auto flex max-w-6xl items-center justify-between px-6 py-4">
          <div className="flex items-center gap-3">
            <div className="flex h-9 w-9 items-center justify-center rounded-xl bg-slate-950 text-white shadow-sm">
              <Code2 size={17} />
            </div>

            <div>
              <p className="text-sm font-semibold tracking-tight">
                Engineering Progress
              </p>
              <p className="text-xs text-slate-500">TruongP</p>
            </div>
          </div>

          <a
            href="https://github.com/Paoying5/fastapi-user-management"
            target="_blank"
            rel="noreferrer"
            className="flex items-center gap-2 rounded-full border border-slate-200 bg-white px-4 py-2 text-sm font-medium text-slate-700 shadow-sm transition hover:-translate-y-0.5 hover:border-slate-300 hover:shadow-md"
          >
            <GitBranch size={15} />
            GitHub
            <ArrowUpRight size={14} />
          </a>
        </div>
      </header>

      <div className="relative mx-auto max-w-6xl px-6">
        {/* Hero */}
        <section className="flex min-h-[78vh] items-center py-24">
          <motion.div
            initial="hidden"
            animate="show"
            variants={container}
            className="max-w-4xl"
          >
            <motion.div
              variants={item}
              className="mb-7 inline-flex items-center gap-2 rounded-full border border-indigo-100 bg-indigo-50/80 px-3.5 py-1.5 text-xs font-medium text-indigo-700"
            >
              <span className="relative flex h-2 w-2">
                <span className="absolute inline-flex h-full w-full animate-ping rounded-full bg-indigo-400 opacity-50" />
                <span className="relative inline-flex h-2 w-2 rounded-full bg-indigo-500" />
              </span>
              Currently learning SQL Analytics
            </motion.div>

            <motion.p
              variants={item}
              className="mb-4 text-sm font-semibold uppercase tracking-[0.22em] text-slate-500"
            >
              FastAPI User Management
            </motion.p>

            <motion.h1
              variants={item}
              className="max-w-4xl text-5xl font-semibold tracking-[-0.045em] text-slate-950 sm:text-6xl md:text-7xl"
            >
              Building systems.
              <br />
              <span className="bg-gradient-to-r from-indigo-600 via-violet-600 to-indigo-500 bg-clip-text text-transparent">
                Learning from data.
              </span>
            </motion.h1>

            <motion.p
              variants={item}
              className="mt-7 max-w-2xl text-base leading-8 text-slate-600 sm:text-lg"
            >
              A practical engineering journey from FastAPI backend development
              to PostgreSQL, automated testing, SQL analytics, and data-driven
              thinking.
            </motion.p>

            <motion.div
              variants={item}
              className="mt-10 flex flex-wrap gap-3"
            >
              <a
                href="#latest"
                className="inline-flex items-center gap-2 rounded-full bg-slate-950 px-6 py-3 text-sm font-medium text-white shadow-lg shadow-slate-950/10 transition hover:-translate-y-0.5 hover:bg-slate-800"
              >
                View latest progress
                <ArrowUpRight size={16} />
              </a>

              <a
                href="#journey"
                className="inline-flex items-center gap-2 rounded-full border border-slate-200 bg-white/80 px-6 py-3 text-sm font-medium text-slate-700 shadow-sm transition hover:-translate-y-0.5 hover:bg-white hover:shadow-md"
              >
                Learning journey
              </a>
            </motion.div>
          </motion.div>
        </section>

        {/* Status strip */}
        <motion.section
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, amount: 0.2 }}
          transition={{ duration: 0.6 }}
          className="mb-24 grid overflow-hidden rounded-3xl border border-slate-200/80 bg-white/80 shadow-xl shadow-slate-200/40 backdrop-blur md:grid-cols-4"
        >
          {[
            ["Backend", "Completed"],
            ["Database", "Stable"],
            ["Regression", "79 / 79 Passed"],
            ["Analytics", "In Progress"],
          ].map(([label, value], index) => (
            <div
              key={label}
              className={`p-6 ${
                index < 3 ? "border-b border-slate-100 md:border-b-0 md:border-r" : ""
              }`}
            >
              <p className="text-xs font-medium uppercase tracking-[0.15em] text-slate-400">
                {label}
              </p>
              <p className="mt-2 text-base font-semibold text-slate-900">
                {value}
              </p>
            </div>
          ))}
        </motion.section>

        {/* Analytics */}
        <section className="mb-28">
          <div className="mb-8 flex items-end justify-between gap-6">
            <div>
              <p className="mb-2 text-xs font-semibold uppercase tracking-[0.2em] text-indigo-600">
                Analytics Snapshot
              </p>
              <h2 className="text-3xl font-semibold tracking-tight text-slate-950">
                Progress you can measure.
              </h2>
            </div>

            <p className="hidden max-w-md text-right text-sm leading-6 text-slate-500 md:block">
              Current values are based on the synthetic analytics dataset used
              for SQL practice.
            </p>
          </div>

          <motion.div
            variants={container}
            initial="hidden"
            whileInView="show"
            viewport={{ once: true, amount: 0.25 }}
            className="grid gap-4 sm:grid-cols-2 lg:grid-cols-4"
          >
            {stats.map((stat) => {
              const Icon = stat.icon;

              return (
                <motion.div
                  variants={item}
                  key={stat.label}
                  whileHover={{
                    y: -6,
                    transition: { duration: 0.2 },
                  }}
                  className="group relative overflow-hidden rounded-3xl border border-slate-200/80 bg-white p-6 shadow-sm transition-shadow hover:shadow-xl hover:shadow-indigo-100/50"
                >
                  <div className="absolute right-[-3rem] top-[-3rem] h-28 w-28 rounded-full bg-indigo-100/0 blur-2xl transition group-hover:bg-indigo-100/80" />

                  <div className="relative">
                    <div className="mb-8 flex h-10 w-10 items-center justify-center rounded-2xl bg-slate-50 text-slate-600 ring-1 ring-slate-100">
                      <Icon size={18} />
                    </div>

                    <p className="text-4xl font-semibold tracking-[-0.04em] text-slate-950">
                      {stat.value}
                    </p>

                    <p className="mt-2 text-sm font-medium text-slate-700">
                      {stat.label}
                    </p>

                    <p className="mt-1 text-xs text-slate-400">
                      {stat.description}
                    </p>
                  </div>
                </motion.div>
              );
            })}
          </motion.div>
        </section>

        {/* Latest Week */}
        <section id="latest" className="mb-28 scroll-mt-24">
          <motion.div
            initial={{ opacity: 0, y: 35 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true, amount: 0.2 }}
            transition={{ duration: 0.65 }}
            className="overflow-hidden rounded-[2rem] border border-slate-200 bg-slate-950 text-white shadow-2xl shadow-slate-300/60"
          >
            <div className="grid lg:grid-cols-[0.85fr_1.15fr]">
              <div className="border-b border-white/10 p-8 sm:p-10 lg:border-b-0 lg:border-r lg:p-12">
                <div className="mb-12 flex items-center justify-between">
                  <span className="rounded-full bg-white/10 px-3 py-1 text-xs font-medium text-white/70">
                    W25
                  </span>

                  <span className="flex items-center gap-2 text-xs font-medium text-emerald-300">
                    <CheckCircle2 size={14} />
                    Completed
                  </span>
                </div>

                <p className="text-xs uppercase tracking-[0.18em] text-white/40">
                  12 Oct — 18 Oct 2026
                </p>

                <h2 className="mt-4 text-3xl font-semibold tracking-tight sm:text-4xl">
                  Backend lifecycle
                  <br />
                  <span className="text-indigo-300">→ Data Analytics</span>
                </h2>

                <p className="mt-6 max-w-md text-sm leading-7 text-white/55">
                  Reached the planned backend milestone, completed regression
                  verification, and moved the project toward practical SQL
                  analytics.
                </p>
              </div>

              <div className="p-8 sm:p-10 lg:p-12">
                <p className="mb-6 text-xs font-semibold uppercase tracking-[0.18em] text-white/40">
                  Weekly highlights
                </p>

                <div className="grid gap-3 sm:grid-cols-2">
                  {weekHighlights.map((highlight, index) => (
                    <motion.div
                      key={highlight}
                      initial={{ opacity: 0, x: 15 }}
                      whileInView={{ opacity: 1, x: 0 }}
                      viewport={{ once: true }}
                      transition={{
                        duration: 0.4,
                        delay: index * 0.05,
                      }}
                      className="flex gap-3 rounded-2xl border border-white/10 bg-white/[0.04] p-4"
                    >
                      <CheckCircle2
                        size={17}
                        className="mt-0.5 shrink-0 text-indigo-300"
                      />

                      <span className="text-sm leading-6 text-white/70">
                        {highlight}
                      </span>
                    </motion.div>
                  ))}
                </div>
              </div>
            </div>
          </motion.div>
        </section>

        {/* Insight */}
        <section className="mb-28">
          <motion.div
            initial={{ opacity: 0, scale: 0.98 }}
            whileInView={{ opacity: 1, scale: 1 }}
            viewport={{ once: true, amount: 0.3 }}
            transition={{ duration: 0.6 }}
            className="relative overflow-hidden rounded-[2rem] border border-indigo-100 bg-gradient-to-br from-indigo-50 via-white to-violet-50 p-8 sm:p-12"
          >
            <Sparkles className="mb-8 text-indigo-500" size={24} />

            <p className="mb-4 text-xs font-semibold uppercase tracking-[0.2em] text-indigo-600">
              This week I learned
            </p>

            <blockquote className="max-w-4xl text-2xl font-medium leading-[1.45] tracking-tight text-slate-900 sm:text-3xl">
              “A technically correct SQL query does not automatically produce
              a valid business insight.”
            </blockquote>

            <div className="mt-10 flex flex-wrap gap-2">
              {[
                "Data origin",
                "Data quality",
                "Generation logic",
                "Business context",
              ].map((tag) => (
                <span
                  key={tag}
                  className="rounded-full border border-indigo-100 bg-white/70 px-4 py-2 text-xs font-medium text-slate-600"
                >
                  {tag}
                </span>
              ))}
            </div>
          </motion.div>
        </section>

        {/* Roadmap */}
        <section id="journey" className="mb-32 scroll-mt-24">
          <div className="mb-10">
            <p className="mb-2 text-xs font-semibold uppercase tracking-[0.2em] text-indigo-600">
              Learning Journey
            </p>

            <h2 className="text-3xl font-semibold tracking-tight text-slate-950">
              Building one layer at a time.
            </h2>
          </div>

          <div className="relative max-w-3xl">
            <div className="absolute bottom-5 left-[11px] top-5 w-px bg-slate-200" />

            <motion.div
              initial={{ scaleY: 0 }}
              whileInView={{ scaleY: 1 }}
              viewport={{ once: true, amount: 0.25 }}
              transition={{ duration: 1.1 }}
              className="absolute left-[11px] top-5 h-[56%] w-px origin-top bg-indigo-500"
            />

            <div className="space-y-2">
              {roadmap.map((step, index) => (
                <motion.div
                  key={step.title}
                  initial={{ opacity: 0, x: 20 }}
                  whileInView={{ opacity: 1, x: 0 }}
                  viewport={{ once: true }}
                  transition={{
                    delay: index * 0.07,
                    duration: 0.4,
                  }}
                  className="relative flex gap-6 rounded-2xl p-4 transition hover:bg-white"
                >
                  <div className="relative z-10 mt-1 bg-[#f8fafc] py-1">
                    {step.status === "completed" ? (
                      <CheckCircle2
                        size={23}
                        className="text-indigo-600"
                      />
                    ) : step.status === "current" ? (
                      <div className="flex h-[23px] w-[23px] items-center justify-center">
                        <span className="absolute h-5 w-5 animate-ping rounded-full bg-indigo-400/30" />
                        <span className="relative h-3 w-3 rounded-full bg-indigo-600" />
                      </div>
                    ) : (
                      <Circle size={23} className="text-slate-300" />
                    )}
                  </div>

                  <div>
                    <p className="text-base font-medium text-slate-900">
                      {step.title}
                    </p>

                    <p className="mt-1 text-xs font-medium uppercase tracking-[0.12em] text-slate-400">
                      {step.status}
                    </p>
                  </div>
                </motion.div>
              ))}
            </div>
          </div>
        </section>

        {/* Footer */}
        <footer className="border-t border-slate-200 py-10">
          <div className="flex flex-col justify-between gap-4 text-sm text-slate-400 sm:flex-row">
            <p>FastAPI User Management · Learning Progress</p>

            <p>Backend → Data Analytics · 2026</p>
          </div>
        </footer>
      </div>
    </main>
  );
}