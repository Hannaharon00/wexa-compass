import { useMemo, useState } from "react";
import type { SkillNeighbor } from "../types";
import { categoryStyle } from "../lib/categoryColors";

const SIZE = 620;
const CENTER = SIZE / 2;
// Kept well inside the viewBox edge (not SIZE/2) so a wide label pill on
// an outer-ring node -- which can extend ~80px past the node's own
// center point -- never gets clipped by the SVG boundary.
const RADIUS_BY_HOP: Record<number, number> = { 1: 150, 2: 225, 3: 225 };
const MAX_LABEL = 20;

interface Positioned extends SkillNeighbor {
  x: number;
  y: number;
}

