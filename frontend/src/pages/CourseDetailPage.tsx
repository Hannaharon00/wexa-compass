import { Link, useParams } from "react-router-dom";
import { useApiQuery } from "../api/hooks";
import type { Course, CoursePrerequisite } from "../types";
import { EmptyState, ErrorState, LoadingState } from "../components/StateViews";

