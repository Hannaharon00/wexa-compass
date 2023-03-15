import { Link } from "react-router-dom";
import { useApiQuery } from "../api/hooks";
import type { Skill } from "../types";
import SkillPicker from "../components/SkillPicker";
import { LoadingState, ErrorState } from "../components/StateViews";
import { useKnownSkillsContext } from "../state/KnownSkillsContext";

export default function HomePage() {
  const { data: skills, loading, error, refetch } = useApiQuery<Skill[]>("/skills");
  const { knownSkillIds, toggle, clear } = useKnownSkillsContext();

