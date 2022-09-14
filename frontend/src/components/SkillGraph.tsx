import { useMemo, useState } from "react";
import type { SkillNeighbor } from "../types";
import { categoryStyle } from "../lib/categoryColors";

interface Positioned extends SkillNeighbor {
  x: number;
  y: number;
}

