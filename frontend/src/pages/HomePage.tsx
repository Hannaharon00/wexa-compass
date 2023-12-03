import { Link } from "react-router-dom";
import { useApiQuery } from "../api/hooks";
import type { Skill } from "../types";
import SkillPicker from "../components/SkillPicker";
import { LoadingState, ErrorState } from "../components/StateViews";
import { useKnownSkillsContext } from "../state/KnownSkillsContext";

export default function HomePage() {
  const { data: skills, loading, error, refetch } = useApiQuery<Skill[]>("/skills");
  const { knownSkillIds, toggle, clear } = useKnownSkillsContext();

  return (
    <div className="animate-fade-in">
      <section className="mb-12 grid gap-8 lg:grid-cols-[1.1fr_0.9fr] lg:items-center">
        <div>
          <p className="mb-3 text-xs font-semibold uppercase tracking-widest text-indigo-600">Graph-powered career planning</p>
          <h1 className="font-display text-4xl font-semibold leading-tight text-slate-900 sm:text-5xl">
            Find the shortest path to your next role.
          </h1>
          <p className="mt-4 max-w-xl text-base text-slate-600">
            Career Compass models skills, courses and job roles as a connected graph — not a spreadsheet. Tell it what
            you already know, and it traverses the graph to find which roles you're closest to and exactly which
            courses close the gap, in the right order.
          </p>
          <div className="mt-6 flex flex-wrap gap-3">
            <Link to="/roles" className="rounded-full bg-indigo-600 px-5 py-2.5 text-sm font-semibold text-white shadow-sm transition hover:bg-indigo-700">
              Explore roles →
            </Link>
            <Link to="/skills" className="rounded-full border border-slate-300 bg-white px-5 py-2.5 text-sm font-semibold text-slate-700 transition hover:border-indigo-300 hover:text-indigo-700">
              Explore the skill graph
            </Link>
          </div>
        </div>
        <div className="rounded-3xl border border-indigo-100 bg-gradient-to-br from-indigo-50 to-white p-6 text-sm text-slate-600 shadow-sm">
          <p className="font-display text-base font-semibold text-slate-900">How it works</p>
          <ol className="mt-3 space-y-2.5">
            <li className="flex gap-2.5"><span className="mt-0.5 flex h-5 w-5 shrink-0 items-center justify-center rounded-full bg-indigo-600 text-[11px] font-bold text-white">1</span>Pick the skills you already have below.</li>
            <li className="flex gap-2.5"><span className="mt-0.5 flex h-5 w-5 shrink-0 items-center justify-center rounded-full bg-indigo-600 text-[11px] font-bold text-white">2</span>Browse roles ranked by how much of the required skill set you already match.</li>
            <li className="flex gap-2.5"><span className="mt-0.5 flex h-5 w-5 shrink-0 items-center justify-center rounded-full bg-indigo-600 text-[11px] font-bold text-white">3</span>Open a role to get an ordered course plan for exactly what's missing.</li>
          </ol>
        </div>
      </section>

      <section className="rounded-3xl border border-slate-200 bg-white p-6 shadow-sm sm:p-8">
        <div className="mb-5 flex items-center justify-between gap-4">
          <div>
            <h2 className="font-display text-xl font-semibold text-slate-900">What do you already know?</h2>
            <p className="mt-1 text-sm text-slate-500">Your selections are saved on this device and used across the whole app.</p>
          </div>
          {knownSkillIds.length > 0 && (
            <button onClick={clear} className="shrink-0 rounded-full border border-slate-200 px-3 py-1.5 text-xs font-medium text-slate-500 hover:border-red-200 hover:text-red-600">
              Clear all
            </button>
          )}
        </div>

        {loading && <LoadingState label="Loading skills…" />}
        {error && <ErrorState message={error} onRetry={refetch} />}
        {skills && <SkillPicker skills={skills} selected={knownSkillIds} onToggle={toggle} />}
      </section>
    </div>
  );
}
