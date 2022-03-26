import { useMemo, useState } from "react";
import type { Skill } from "../types";
import { categoryStyle } from "../lib/categoryColors";

export default function SkillPicker({
  skills,
  selected,
  onToggle,
}: {
  skills: Skill[];
  selected: string[];
  onToggle: (skillId: string) => void;
}) {
  const [query, setQuery] = useState("");
  const selectedSet = useMemo(() => new Set(selected), [selected]);

