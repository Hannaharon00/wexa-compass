export interface Skill {
  skill_id: string;
  name: string;
  category: string | null;
  description: string | null;
}

export interface SkillNeighbor {
  skill_id: string;
  name: string;
  category: string | null;
  hops: number;
  courses: { course_id: string; title: string }[];
}

