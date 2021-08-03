import { useCallback, useEffect, useState } from "react";
import { api, ApiError } from "./client";

interface QueryState<T> {
  data: T | null;
  loading: boolean;
  error: string | null;
}

