import { useMemo, useState } from "react";
import { useApiQuery } from "../api/hooks";
import type { Course } from "../types";
import CourseCard from "../components/CourseCard";
import { EmptyState, ErrorState, SkeletonCard } from "../components/StateViews";

const LEVELS = ["Beginner", "Intermediate", "Advanced"];

export default function CoursesPage() {
  const { data: courses, loading, error, refetch } = useApiQuery<Course[]>("/courses");
  const [query, setQuery] = useState("");
  const [level, setLevel] = useState<string | null>(null);

  const filtered = useMemo(() => {
    if (!courses) return [];
    const q = query.trim().toLowerCase();
    return courses.filter((c) => {
      if (level && c.level !== level) return false;
      if (q && !c.title.toLowerCase().includes(q) && !c.teaches.some((s) => s.toLowerCase().includes(q))) return false;
      return true;
    });
  }, [courses, query, level]);

