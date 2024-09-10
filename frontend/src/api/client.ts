export class ApiError extends Error {
  status: number;
  constructor(message: string, status: number) {
    super(message);
    this.status = status;
  }
}

// When frontend and backend are deployed separately (e.g. Vercel +
// Railway), VITE_API_BASE_URL points at the backend's own /api. Left
// unset, it falls back to a same-origin relative path -- which is what
// local dev (via the Vite proxy) and a single-service deploy both want.
const API_BASE = import.meta.env.VITE_API_BASE_URL ?? "/api";

