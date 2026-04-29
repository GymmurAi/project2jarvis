"use client";

import { Card } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Separator } from "@/components/ui/separator";
import { useState } from "react";

// KPI Data
const kpis = [
  {
    title: "Total Active Projects",
    value: "24",
    change: "+12%",
    trend: "up",
    status: "green",
    subtext: "vs last month",
  },
  {
    title: "Total Revenue (MTD)",
    value: "$184,200",
    change: "+18%",
    trend: "up",
    status: "green",
    subtext: "vs last month",
  },
  {
    title: "Team Utilization",
    value: "78%",
    change: "-3%",
    trend: "down",
    status: "yellow",
    subtext: "vs target 85%",
  },
  {
    title: "AI Agent Score",
    value: "94.2",
    change: "+2.1",
    trend: "up",
    status: "green",
    subtext: "out of 100",
  },
];

// Activity Feed
const activities = [
  {
    time: "2 min ago",
    agent: "Builder",
    action: "Completed feature: User auth system",
    type: "success",
  },
  {
    time: "15 min ago",
    agent: "Researcher",
    action: "Updated decisions-log.md with new ADR",
    type: "info",
  },
  {
    time: "1 hour ago",
    agent: "Council",
    action: "Security review passed for API v2.1",
    type: "success",
  },
  {
    time: "2 hours ago",
    agent: "Maintainer",
    action: "Dependencies updated (12 packages)",
    type: "info",
  },
  {
    time: "3 hours ago",
    agent: "Builder",
    action: "Fixed critical bug in payment module",
    type: "warning",
  },
  {
    time: "4 hours ago",
    agent: "Client",
    action: "New project request: E-commerce platform",
    type: "client",
  },
];

// AI Agent Usage
const agentUsage = [
  { name: "Builder", tasks: 342, trend: "+15%", color: "#0EA5E9" },
  { name: "Researcher", tasks: 198, trend: "+8%", color: "#10B981" },
  { name: "Maintainer", tasks: 156, trend: "+12%", color: "#F59E0B" },
  { name: "Council", tasks: 89, trend: "+5%", color: "#8B5CF6" },
];

export default function ExecutiveDashboard() {
  const [selectedKpi, setSelectedKpi] = useState<number | null>(null);
  const [lastUpdated] = useState(new Date().toLocaleTimeString());

  const drillDownData = {
    0: { // Total Active Projects
      chart: [24, 22, 25, 23, 24, 26, 24],
      labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
      detail: "24 active projects across 8 clients. 4 projects in final review, 12 in development, 8 in planning."
    },
    1: { // Total Revenue
      chart: [142000, 156000, 163000, 171000, 178000, 182000, 184200],
      labels: ['Week 1', 'Week 2', 'Week 3', 'Week 4', 'Week 5', 'Week 6', 'Week 7'],
      detail: "MTD Revenue: $184,200. Projected monthly total: $235k. Top client: Acme Corp ($45k)."
    },
    2: { // Team Utilization
      chart: [82, 79, 81, 78, 76, 78, 78],
      labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
      detail: "Current: 78%. Target: 85%. 3 team members overallocated (>90%). 2 members underallocated (<60%)."
    },
    3: { // AI Agent Score
      chart: [92.1, 92.8, 93.2, 93.5, 93.9, 94.0, 94.2],
      labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
      detail: "AI Agent Score: 94.2/100. Builder: 96.1, Researcher: 93.8, Maintainer: 92.5, Council: 94.4."
    }
  };

  return (
    <div className="min-h-screen bg-[#0F172A] text-[#F8FAFC]">
      {/* Header */}
      <header className="sticky top-0 z-50 bg-[#0F172A]/90 backdrop-blur-md border-b border-[#1E293B]">
        <div className="container mx-auto max-w-[1400px] px-4 md:px-6">
          <div className="flex items-center justify-between min-h-[64px] gap-6">
            <div className="flex items-center gap-2 text-xl font-extrabold text-[#F8FAFC]">
              <div className="w-8 h-8 text-[#0EA5E9]">
                <svg viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg" className="w-full h-full">
                  <rect width="32" height="32" rx="8" fill="currentColor"/>
                  <path d="M10 16L14 20L22 12" stroke="white" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round"/>
                </svg>
              </div>
              <span>Project2Jarvis</span>
            </div>
            <nav className="hidden md:flex items-center gap-6" role="navigation">
              <a href="#" className="flex items-center min-h-[44px] text-[#94A3B8] text-sm font-semibold hover:text-[#0EA5E9] transition-colors">
                Dashboard
              </a>
              <a href="#" className="flex items-center min-h-[44px] text-[#94A3B8] text-sm font-semibold hover:text-[#0EA5E9] transition-colors">
                Projects
              </a>
              <a href="#" className="flex items-center min-h-[44px] text-[#94A3B8] text-sm font-semibold hover:text-[#0EA5E9] transition-colors">
                Clients
              </a>
              <a href="#" className="flex items-center min-h-[44px] text-[#94A3B8] text-sm font-semibold hover:text-[#0EA5E9] transition-colors">
                Agents
              </a>
            </nav>
            <div className="flex gap-4 items-center">
              <button className="inline-flex items-center justify-center min-h-[44px] px-6 py-3 bg-[#10B981] text-white text-sm font-semibold rounded-lg hover:bg-[#059669] transition-all cursor-pointer">
                New Project
              </button>
            </div>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="container mx-auto max-w-[1400px] px-4 md:px-6 py-6 md:py-8">
        {/* Page Title */}
        <div className="mb-6 md:mb-8">
          <h1 className="text-2xl md:text-3xl font-extrabold text-[#F8FAFC] mb-2">
            Executive Command Center
          </h1>
          <p className="text-sm text-[#94A3B8]">
            Real-time overview of agency health and activity. Last updated: {lastUpdated}
          </p>
        </div>

        {/* KPI Cards - Top Row (Inverted Pyramid) */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 md:gap-6 mb-6 md:mb-8">
          {kpis.map((kpi, index) => (
            <Card 
              key={index} 
              onClick={() => setSelectedKpi(selectedKpi === index ? null : index)}
              className={`bg-[#1E293B] border-[#334155] hover:border-[#0EA5E9] transition-all cursor-pointer hover:-translate-y-1 ${
                selectedKpi === index ? 'ring-2 ring-[#0EA5E9] border-[#0EA5E9]' : ''
              }`}
            >
              <div className="p-4 md:p-6">
                <div className="flex items-center justify-between mb-2">
                  <p className="text-sm text-[#94A3B8] font-medium">{kpi.title}</p>
                  <Badge className={`
                    ${kpi.status === 'green' ? 'bg-[#10B981]/20 text-[#10B981] border-[#10B981]/30' : ''}
                    ${kpi.status === 'yellow' ? 'bg-[#F59E0B]/20 text-[#F59E0B] border-[#F59E0B]/30' : ''}
                    text-xs font-semibold
                  `}>
                    {kpi.trend === 'up' ? '↑' : '↓'} {kpi.change}
                  </Badge>
                </div>
                <p className="text-3xl md:text-4xl font-extrabold text-[#F8FAFC] mb-1">
                  {kpi.value}
                </p>
                <p className="text-xs text-[#64748B]">{kpi.subtext}</p>
              </div>
            </Card>
          ))}
        </div>

        {/* Drill-Down Section */}
        {selectedKpi !== null && drillDownData[selectedKpi as keyof typeof drillDownData] && (
          <Card className="bg-[#1E293B] border-[#334155] mb-6 md:mb-8 animate-slideDown">
            <div className="p-4 md:p-6">
              <div className="flex items-center justify-between mb-4">
                <h3 className="text-lg font-bold text-[#F8FAFC]">
                  {kpis[selectedKpi].title} - Detailed View
                </h3>
                <button 
                  onClick={() => setSelectedKpi(null)}
                  className="text-[#94A3B8] hover:text-[#F8FAFC] transition-colors"
                >
                  <svg className="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                    <path d="M18 6L6 18M6 6l12 12"/>
                  </svg>
                </button>
              </div>
              
              {/* Chart Visualization */}
              <div className="bg-[#0F172A] rounded-lg p-4 md:p-6 mb-4">
                <div className="flex items-end gap-2 h-32 md:h-40">
                  {drillDownData[selectedKpi as keyof typeof drillDownData].chart.map((value: number, i: number) => {
                    const max = Math.max(...drillDownData[selectedKpi as keyof typeof drillDownData].chart);
                    const height = (value / max) * 100;
                    return (
                      <div key={i} className="flex-1 flex flex-col items-center gap-2">
                        <div 
                          className="w-full rounded-t bg-[#0EA5E9] opacity-80 hover:opacity-100 transition-opacity"
                          style={{ height: `${height}%` }}
                        />
                        <span className="text-xs text-[#94A3B8]">
                          {drillDownData[selectedKpi as keyof typeof drillDownData].labels[i]}
                        </span>
                      </div>
                    );
                  })}
                </div>
              </div>
              
              {/* Detail Text */}
              <p className="text-sm text-[#94A3B8]">
                {drillDownData[selectedKpi as keyof typeof drillDownData].detail}
              </p>
            </div>
          </Card>
        )}

        {/* Middle Section: AI Overview + Activity Feed */}
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-4 md:gap-6 mb-6 md:mb-8">
          {/* AI Agent Overview - 2/3 width */}
          <div className="lg:col-span-2">
            <Card className="bg-[#1E293B] border-[#334155]">
              <div className="p-4 md:p-6">
                <h2 className="text-lg font-bold text-[#F8FAFC] mb-4">AI Agent Overview</h2>
                {/* Chart Placeholder */}
                <div className="bg-[#0F172A] rounded-lg p-4 md:p-6 mb-4" style={{ minHeight: '200px' }}>
                  <div className="flex items-end gap-2 h-32 md:h-40">
                    {agentUsage.map((agent, i) => (
                      <div key={i} className="flex-1 flex flex-col items-center gap-2">
                        <div 
                          className="w-full rounded-t" 
                          style={{ 
                            height: `${60 + Math.random() * 40}%`, 
                            backgroundColor: agent.color,
                            opacity: 0.8 
                          }}
                        />
                        <span className="text-xs text-[#94A3B8]">{agent.name}</span>
                      </div>
                    ))}
                  </div>
                </div>
                {/* Agent Stats */}
                <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
                  {agentUsage.map((agent, i) => (
                    <div key={i} className="text-center">
                      <p className="text-sm text-[#94A3B8] mb-1">{agent.name}</p>
                      <p className="text-lg md:text-xl font-bold text-[#F8FAFC]">{agent.tasks}</p>
                      <p className="text-xs text-[#10B981]">{agent.trend}</p>
                    </div>
                  ))}
                </div>
              </div>
            </Card>
          </div>

          {/* Real-Time Activity Feed - 1/3 width */}
          <div className="lg:col-span-1">
            <Card className="bg-[#1E293B] border-[#334155] h-full">
              <div className="p-4 md:p-6">
                <h2 className="text-lg font-bold text-[#F8FAFC] mb-4">Live Activity Feed</h2>
                <div className="space-y-4">
                  {activities.map((activity, i) => (
                    <div key={i} className="flex gap-3">
                      <div className={`
                        w-2 h-2 rounded-full mt-1.5 flex-shrink-0
                        ${activity.type === 'success' ? 'bg-[#10B981]' : ''}
                        ${activity.type === 'warning' ? 'bg-[#F59E0B]' : ''}
                        ${activity.type === 'info' ? 'bg-[#0EA5E9]' : ''}
                        ${activity.type === 'client' ? 'bg-[#8B5CF6]' : ''}
                      `} />
                      <div className="flex-1 min-w-0">
                        <p className="text-sm text-[#F8FAFC] font-medium leading-tight">
                          <span className="text-[#94A3B8]">{activity.agent}:</span> {activity.action}
                        </p>
                        <p className="text-xs text-[#64748B] mt-1">{activity.time}</p>
                      </div>
                    </div>
                  ))}
                </div>
                <Separator className="my-4 bg-[#334155]" />
                <button className="w-full inline-flex items-center justify-center min-h-[44px] text-sm text-[#0EA5E9] font-semibold hover:text-[#38BDF8] transition-colors cursor-pointer">
                  View All Activity →
                </button>
              </div>
            </Card>
          </div>
        </div>

        {/* Bottom Section: Quick Actions */}
        <Card className="bg-[#1E293B] border-[#334155]">
          <div className="p-4 md:p-6">
            <h2 className="text-lg font-bold text-[#F8FAFC] mb-4">Quick Actions</h2>
            <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-4">
              <button className="inline-flex items-center justify-center gap-2 min-h-[44px] px-4 py-3 bg-[#1E293B] text-[#F8FAFC] text-sm font-semibold rounded-lg border-2 border-[#334155] hover:border-[#0EA5E9] hover:bg-[#1E293B]/80 transition-all cursor-pointer">
                <svg className="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                  <path d="M12 5v14M5 12h14"/>
                </svg>
                New Project
              </button>
              <button className="inline-flex items-center justify-center gap-2 min-h-[44px] px-4 py-3 bg-[#1E293B] text-[#F8FAFC] text-sm font-semibold rounded-lg border-2 border-[#334155] hover:border-[#0EA5E9] hover:bg-[#1E293B]/80 transition-all cursor-pointer">
                <svg className="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                  <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/>
                </svg>
                Manage Clients
              </button>
              <button className="inline-flex items-center justify-center gap-2 min-h-[44px] px-4 py-3 bg-[#1E293B] text-[#F8FAFC] text-sm font-semibold rounded-lg border-2 border-[#334155] hover:border-[#0EA5E9] hover:bg-[#1E293B]/80 transition-all cursor-pointer">
                <svg className="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                  <rect x="2" y="3" width="20" height="14" rx="2"/><line x1="8" y1="21" x2="16" y2="21"/>
                </svg>
                View Reports
              </button>
              <button className="inline-flex items-center justify-center gap-2 min-h-[44px] px-4 py-3 bg-[#1E293B] text-[#F8FAFC] text-sm font-semibold rounded-lg border-2 border-[#334155] hover:border-[#0EA5E9] hover:bg-[#1E293B]/80 transition-all cursor-pointer">
                <svg className="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                  <circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.5 1.5 0 0 0 .5-2.1 1.54 1.54 0 0 0-3.78-2.1c-.4-.6-.5-1.4-1.2-2.1a1.5 1.5 0 0 0-2.1-.5 1.54 1.54 0 0 0-2.1 3.78c-.6.4-1.4.5-2.1 1.2a1.5 1.5 0 0 0 .5 2.1 1.54 1.54 0 0 0 3.78 2.1c.4.6.5 1.4 1.2 2.1a1.5 1.5 0 0 0 2.1.5 1.54 1.54 0 0 0 2.1-3.78c.6-.4 1.4-.5 2.1-1.2z"/>
                </svg>
                Settings
              </button>
            </div>
          </div>
        </Card>
      </main>
    </div>
  );
}
