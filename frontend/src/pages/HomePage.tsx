import { Link } from "react-router-dom";
import { useApiQuery } from "../api/hooks";
import type { Skill } from "../types";
import SkillPicker from "../components/SkillPicker";
import { LoadingState, ErrorState } from "../components/StateViews";
import { useKnownSkillsContext } from "../state/KnownSkillsContext";

export default function HomePage() {
  const { data: skills, loading, error, refetch } = useApiQuery<Skill[]>("/skills");
  const { knownSkillIds, toggle, clear } = useKnownSkillsContext();

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

