import { useEffect, useMemo, useState } from "react";
import { Link } from "react-router-dom";
import { useApiQuery } from "../api/hooks";
import type { Skill, SkillNeighbor } from "../types";
import { EmptyState, ErrorState, LoadingState } from "../components/StateViews";
import { categoryStyle } from "../lib/categoryColors";
import SkillGraph from "../components/SkillGraph";

