import type { ReactNode } from "react";
import { NavLink } from "react-router-dom";
import { useKnownSkillsContext } from "../state/KnownSkillsContext";

const NAV = [
  { to: "/", label: "Home", end: true },
  { to: "/roles", label: "Roles" },
  { to: "/courses", label: "Courses" },
  { to: "/skills", label: "Skill Graph" },
];

function CompassMark() {
  return (
    <svg width="26" height="26" viewBox="0 0 24 24" fill="none">
      <circle cx="12" cy="12" r="9.25" stroke="currentColor" strokeWidth="1.6" />
      <path d="M15.2 8.8 13 13l-4.2 2.2L11 11l4.2-2.2Z" fill="currentColor" />
    </svg>
  );
}

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

          <nav className="hidden items-center gap-1 sm:flex">
            {NAV.map((item) => (
              <NavLink
                key={item.to}
                to={item.to}
                end={item.end}
                className={({ isActive }) =>
                  `rounded-full px-3.5 py-1.5 text-sm font-medium transition ${
                    isActive ? "bg-indigo-600 text-white shadow-sm" : "text-slate-600 hover:bg-slate-200/70 hover:text-slate-900"
                  }`
                }
              >
                {item.label}
              </NavLink>
            ))}
          </nav>

          <NavLink
            to="/skills"
            className="flex items-center gap-1.5 rounded-full border border-slate-200 bg-white px-3 py-1.5 text-xs font-semibold text-slate-600 shadow-sm transition hover:border-indigo-200 hover:text-indigo-700"
          >
            <span className="h-1.5 w-1.5 rounded-full bg-indigo-500" />
            {knownSkillIds.length} skill{knownSkillIds.length === 1 ? "" : "s"} selected
          </NavLink>
        </div>
        <nav className="flex items-center gap-1 overflow-x-auto px-6 pb-3 sm:hidden">
          {NAV.map((item) => (
            <NavLink
              key={item.to}
              to={item.to}
              end={item.end}
              className={({ isActive }) =>
                `whitespace-nowrap rounded-full px-3 py-1 text-sm font-medium transition ${
                  isActive ? "bg-indigo-600 text-white" : "text-slate-600"
                }`
              }
            >
              {item.label}
            </NavLink>
          ))}
        </nav>
      </header>

      <main className="mx-auto max-w-6xl px-6 py-10">{children}</main>

      <footer className="mx-auto max-w-6xl px-6 py-10 text-xs text-slate-400">
        <p>
          Career Compass is a demo application built for the Wexa AI CognoDB take-home assignment. Data model, seed
          data and every query are documented in the project README.
        </p>
      </footer>
    </div>
  );
}
