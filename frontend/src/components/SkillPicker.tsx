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

  const grouped = useMemo(() => {
    const q = query.trim().toLowerCase();
    const filtered = q ? skills.filter((s) => s.name.toLowerCase().includes(q)) : skills;
    const byCategory = new Map<string, Skill[]>();
    for (const skill of filtered) {
      const key = skill.category ?? "Other";
      if (!byCategory.has(key)) byCategory.set(key, []);
      byCategory.get(key)!.push(skill);
    }
    return [...byCategory.entries()].sort((a, b) => a[0].localeCompare(b[0]));
  }, [skills, query]);

