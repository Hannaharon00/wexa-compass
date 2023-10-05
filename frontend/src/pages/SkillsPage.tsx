import { useEffect, useMemo, useState } from "react";
import { Link } from "react-router-dom";
import { useApiQuery } from "../api/hooks";
import type { Skill, SkillNeighbor } from "../types";
import { EmptyState, ErrorState, LoadingState } from "../components/StateViews";
import { categoryStyle } from "../lib/categoryColors";
import SkillGraph from "../components/SkillGraph";

  const {
    data: neighbors,
    loading: neighborsLoading,
    error: neighborsError,
  } = useApiQuery<SkillNeighbor[]>(selectedId ? `/skills/${selectedId}/neighborhood?depth=${depth}` : null, [selectedId, depth]);

  const selectedSkill = useMemo(() => skills?.find((s) => s.skill_id === selectedId) ?? null, [skills, selectedId]);

