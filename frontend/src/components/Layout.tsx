import type { ReactNode } from "react";
import { NavLink } from "react-router-dom";
import { useKnownSkillsContext } from "../state/KnownSkillsContext";

const NAV = [
  { to: "/", label: "Home", end: true },
  { to: "/roles", label: "Roles" },
  { to: "/courses", label: "Courses" },
  { to: "/skills", label: "Skill Graph" },
];

