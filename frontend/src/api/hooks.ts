import { useCallback, useEffect, useState } from "react";
import { api, ApiError } from "./client";

interface QueryState<T> {
  data: T | null;
  loading: boolean;
  error: string | null;
}

/** Fires a POST request on demand via `mutate(body)`, tracking loading/error. */
export function useApiMutation<TBody, TResult>(path: string) {
  const [state, setState] = useState<QueryState<TResult>>({ data: null, loading: false, error: null });

