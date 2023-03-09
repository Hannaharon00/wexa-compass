import { Link, useParams } from "react-router-dom";
import { useApiQuery } from "../api/hooks";
import type { Course, CoursePrerequisite } from "../types";
import { EmptyState, ErrorState, LoadingState } from "../components/StateViews";

interface CourseWithSkills extends Course {
  requires_skills: { skill_id: string; name: string }[];
}

