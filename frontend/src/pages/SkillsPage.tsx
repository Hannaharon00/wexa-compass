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

