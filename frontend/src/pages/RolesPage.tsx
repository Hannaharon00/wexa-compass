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

  const matchByRole = useMemo(() => {
    const map = new Map<string, RoleRecommendation>();
    recommendations?.forEach((r) => map.set(r.role_id, r));
    return map;
  }, [recommendations]);

  const sortedRoles = useMemo(() => {
    if (!roles) return [];
    if (matchByRole.size === 0) return roles;
    return [...roles].sort((a, b) => (matchByRole.get(b.role_id)?.match_percent ?? 0) - (matchByRole.get(a.role_id)?.match_percent ?? 0));
  }, [roles, matchByRole]);

