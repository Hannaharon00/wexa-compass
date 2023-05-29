import { Link, useParams } from "react-router-dom";
import { useApiQuery } from "../api/hooks";
import type { Course, CoursePrerequisite } from "../types";
import { EmptyState, ErrorState, LoadingState } from "../components/StateViews";

interface CourseWithSkills extends Course {
  requires_skills: { skill_id: string; name: string }[];
}

const LEVEL_STYLE: Record<string, string> = {
  Beginner: "bg-emerald-50 text-emerald-700 border-emerald-200",
  Intermediate: "bg-amber-50 text-amber-700 border-amber-200",
  Advanced: "bg-rose-50 text-rose-700 border-rose-200",
};

