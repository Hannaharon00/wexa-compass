import { useEffect, useMemo } from "react";
import { useApiQuery, useApiMutation } from "../api/hooks";
import type { RoleRecommendation, RoleSummary } from "../types";
import RoleCard from "../components/RoleCard";
import { EmptyState, ErrorState, SkeletonCard } from "../components/StateViews";
import { useKnownSkillsContext } from "../state/KnownSkillsContext";
import { Link } from "react-router-dom";

export default function RolesPage() {
  const { data: roles, loading, error, refetch } = useApiQuery<RoleSummary[]>("/roles");
  const { knownSkillIds } = useKnownSkillsContext();
  const { data: recommendations, mutate: recommend } = useApiMutation<{ known_skill_ids: string[] }, RoleRecommendation[]>(
    "/roles/recommend"
  );

  useEffect(() => {
    if (knownSkillIds.length > 0) {
      recommend({ known_skill_ids: knownSkillIds }).catch(() => {});
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [knownSkillIds.join(",")]);

