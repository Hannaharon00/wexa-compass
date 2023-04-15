import { useEffect } from "react";
import { Link, useParams } from "react-router-dom";
import { useApiMutation, useApiQuery } from "../api/hooks";
import type { LearningPathResult, RoleDetail } from "../types";
import { EmptyState, ErrorState, LoadingState } from "../components/StateViews";
import { categoryStyle } from "../lib/categoryColors";
import { useKnownSkillsContext } from "../state/KnownSkillsContext";

