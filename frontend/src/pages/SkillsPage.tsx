import { useEffect, useMemo, useState } from "react";
import { Link } from "react-router-dom";
import { useApiQuery } from "../api/hooks";
import type { Skill, SkillNeighbor } from "../types";
import { EmptyState, ErrorState, LoadingState } from "../components/StateViews";
import { categoryStyle } from "../lib/categoryColors";
import SkillGraph from "../components/SkillGraph";

export default function SkillsPage() {
  const { data: skills, loading, error, refetch } = useApiQuery<Skill[]>("/skills");
  const [selectedId, setSelectedId] = useState<string | null>(null);
  const [depth, setDepth] = useState(2);
  const [query, setQuery] = useState("");

  useEffect(() => {
    if (!selectedId && skills && skills.length > 0) setSelectedId(skills[0].skill_id);
  }, [skills, selectedId]);

  const {
    data: neighbors,
    loading: neighborsLoading,
    error: neighborsError,
  } = useApiQuery<SkillNeighbor[]>(selectedId ? `/skills/${selectedId}/neighborhood?depth=${depth}` : null, [selectedId, depth]);

  const selectedSkill = useMemo(() => skills?.find((s) => s.skill_id === selectedId) ?? null, [skills, selectedId]);

  const filteredSkills = useMemo(() => {
    if (!skills) return [];
    const q = query.trim().toLowerCase();
    return q ? skills.filter((s) => s.name.toLowerCase().includes(q)) : skills;
  }, [skills, query]);

  if (loading) return <LoadingState label="Loading skill graph…" />;
  if (error) return <ErrorState message={error} onRetry={refetch} />;

          {neighborsLoading && <LoadingState label="Traversing the graph…" />}
          {neighborsError && <ErrorState message={neighborsError} />}
          {!neighborsLoading && neighbors && neighbors.length === 0 && (
            <EmptyState title="No related skills found" description="This skill isn't connected to others in the seed data yet." />
          )}
          {!neighborsLoading && selectedSkill && neighbors && neighbors.length > 0 && (
            <>
              <SkillGraph centerName={selectedSkill.name} neighbors={neighbors} onSelect={setSelectedId} />
              <div className="mt-4 flex flex-wrap gap-2">
                {neighbors.map((n) => (
                  <button
                    key={n.skill_id}
                    onClick={() => setSelectedId(n.skill_id)}
                    className="rounded-full border border-slate-200 px-3 py-1 text-xs font-medium text-slate-600 hover:border-indigo-300 hover:text-indigo-700"
                  >
                    {n.name} · {n.hops} hop{n.hops > 1 ? "s" : ""}
                    {n.courses.length > 0 && n.courses[0].course_id && (
                      <>
                        {" "}
                        ·{" "}
                        <Link to={`/courses/${n.courses[0].course_id}`} className="underline" onClick={(e) => e.stopPropagation()}>
                          {n.courses[0].title}
                        </Link>
                      </>
                    )}
                  </button>
                ))}
              </div>
            </>
          )}
        </div>
      </div>
    </div>
  );
}
