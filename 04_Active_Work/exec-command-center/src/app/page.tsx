import type { Metadata } from "next";
import ExecutiveDashboard from "./dashboard-client";

export const metadata: Metadata = {
  title: "Executive Command Center | Project2Jarvis",
  description: "Real-time AI agency overview dashboard",
};

export default function Page() {
  return <ExecutiveDashboard />;
}
