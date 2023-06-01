import { useEffect, useMemo } from "react";
import { useApiQuery, useApiMutation } from "../api/hooks";
import type { RoleRecommendation, RoleSummary } from "../types";
import RoleCard from "../components/RoleCard";
import { EmptyState, ErrorState, SkeletonCard } from "../components/StateViews";
import { useKnownSkillsContext } from "../state/KnownSkillsContext";
import { Link } from "react-router-dom";

