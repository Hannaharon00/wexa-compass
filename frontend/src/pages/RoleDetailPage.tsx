import { useEffect } from "react";
import { Link, useParams } from "react-router-dom";
import { useApiMutation, useApiQuery } from "../api/hooks";
import type { LearningPathResult, RoleDetail } from "../types";
import { EmptyState, ErrorState, LoadingState } from "../components/StateViews";
import { categoryStyle } from "../lib/categoryColors";
import { useKnownSkillsContext } from "../state/KnownSkillsContext";

const LEVEL_STYLE: Record<string, string> = {
  Beginner: "bg-emerald-50 text-emerald-700 border-emerald-200",
  Intermediate: "bg-amber-50 text-amber-700 border-amber-200",
  Advanced: "bg-rose-50 text-rose-700 border-rose-200",
};

export default function RoleDetailPage() {
  const { roleId } = useParams<{ roleId: string }>();
  const { data: role, loading, error, refetch } = useApiQuery<RoleDetail>(roleId ? `/roles/${roleId}` : null, [roleId]);
  const { knownSkillIds } = useKnownSkillsContext();
  const {
    data: path,
    loading: pathLoading,
    error: pathError,
    mutate: computePath,
  } = useApiMutation<{ known_skill_ids: string[]; target_role_id: string }, LearningPathResult>("/learning-path");

  useEffect(() => {
    if (roleId && knownSkillIds.length > 0) {
      computePath({ known_skill_ids: knownSkillIds, target_role_id: roleId }).catch(() => {});
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [roleId, knownSkillIds.join(",")]);

  return (
    <div className="animate-fade-in">
      <Link to="/roles" className="mb-4 inline-flex items-center gap-1 text-sm text-slate-500 hover:text-indigo-600">
        ← All roles
      </Link>

        {knownSkillIds.length > 0 && pathLoading && <LoadingState label="Computing the shortest path through the course graph…" />}
        {pathError && <ErrorState message={pathError} onRetry={() => computePath({ known_skill_ids: knownSkillIds, target_role_id: roleId! })} />}

