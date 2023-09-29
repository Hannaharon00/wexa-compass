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

function Label({
  text,
  y,
  fontSize,
  bold,
}: {
  text: string;
  y: number;
  fontSize: number;
  bold?: boolean;
}) {
  const label = truncate(text);
  const paddingX = 7;
  const width = estimateTextWidth(label, fontSize) + paddingX * 2;
  const height = fontSize + 10;
  return (
    <g pointerEvents="none">
      <rect
        x={-width / 2}
        y={y}
        width={width}
        height={height}
        rx={height / 2}
        className="fill-white stroke-slate-200"
        strokeWidth={1}
      />
      <text
        x={0}
        y={y + height / 2}
        textAnchor="middle"
        dominantBaseline="central"
        fontSize={fontSize}
        fontWeight={bold ? 700 : 600}
        className="fill-slate-700"
      >
        {label}
      </text>
    </g>
  );
}

