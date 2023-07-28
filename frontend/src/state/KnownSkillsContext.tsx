import { createContext, useContext, type ReactNode } from "react";
import { useKnownSkills } from "./useKnownSkills";

type KnownSkillsValue = ReturnType<typeof useKnownSkills>;

const KnownSkillsContext = createContext<KnownSkillsValue | null>(null);

