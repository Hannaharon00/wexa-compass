import { useCallback, useEffect, useState } from "react";

const STORAGE_KEY = "career-compass:known-skills";

function readInitial(): string[] {
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    return raw ? (JSON.parse(raw) as string[]) : [];
  } catch {
    return [];
  }
}

