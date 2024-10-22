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

export default function CourseDetailPage() {
  const { courseId } = useParams<{ courseId: string }>();
  const { data: course, loading, error, refetch } = useApiQuery<CourseWithSkills>(courseId ? `/courses/${courseId}` : null, [courseId]);
  const { data: chain, loading: chainLoading } = useApiQuery<CoursePrerequisite[]>(
    courseId ? `/courses/${courseId}/prerequisites` : null,
    [courseId]
  );

  if (loading) return <LoadingState label="Loading course…" />;
  if (error) return <ErrorState message={error} onRetry={refetch} />;
  if (!course) return null;

  return (
    <div className="animate-fade-in">
      <Link to="/courses" className="mb-4 inline-flex items-center gap-1 text-sm text-slate-500 hover:text-indigo-600">
        ← All courses
      </Link>

