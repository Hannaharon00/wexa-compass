import { useMemo, useState } from "react";
import { useApiQuery } from "../api/hooks";
import type { Course } from "../types";
import CourseCard from "../components/CourseCard";
import { EmptyState, ErrorState, SkeletonCard } from "../components/StateViews";

