import type { ReactNode } from "react";
import { NavLink } from "react-router-dom";
import { useKnownSkillsContext } from "../state/KnownSkillsContext";

const NAV = [
  { to: "/", label: "Home", end: true },
  { to: "/roles", label: "Roles" },
  { to: "/courses", label: "Courses" },
  { to: "/skills", label: "Skill Graph" },
];

export default function Layout({ children }: { children: ReactNode }) {
  const { knownSkillIds } = useKnownSkillsContext();

  return (
    <div className="min-h-screen bg-slate-50">
      <header className="sticky top-0 z-30 border-b border-slate-200/70 bg-slate-50/85 backdrop-blur">
        <div className="mx-auto flex max-w-6xl items-center justify-between px-6 py-4">
          <NavLink to="/" className="flex items-center gap-2 text-slate-900">
            <span className="flex h-8 w-8 items-center justify-center rounded-full bg-indigo-600 text-white">
              <CompassMark />
            </span>
            <span className="font-display text-lg font-semibold tracking-tight">Career Compass</span>
          </NavLink>

