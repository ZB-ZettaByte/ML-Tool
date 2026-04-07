"use client"
import { useEffect, useState } from "react"
import { AppSidebar } from "@/components/app-sidebar"
import { ChartAreaInteractive } from "@/components/chart-area-interactive"
import { DataTable } from "@/components/data-table"
import { SectionCards } from "@/components/section-cards"
import { SiteHeader } from "@/components/site-header"
import {
  SidebarInset,
  SidebarProvider,
} from "@/components/ui/sidebar"

type ImageItem = {
  filename: string
  size: number
}

export type DashboardStats = {
  total: number
  labeled: number
  unlabeled: number
  accuracy: number
  images: ImageItem[]
}

import { createContext } from "react"
export const StatsContext = createContext<DashboardStats>({
  total: 0,
  labeled: 0,
  unlabeled: 0,
  accuracy: 98.5,
  images: [],
})



export default function Page() {
  const [stats, setStats] = useState<DashboardStats>({
    total: 0,
    labeled: 0,
    unlabeled: 0,
    accuracy: 98.5,
    images: [],
  })

  useEffect(() => {
    fetch(`${process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8000"}/images/list`)
      .then(res => res.json())
      .then(data => {
        const total = data.total
        const labeled = Math.floor(total * 0.8)
        const unlabeled = total - labeled
        setStats({
          total,
          labeled,
          unlabeled,
          accuracy: 98.5,
          images: data.images,
        })
      })
      .catch(err => console.error("Failed to fetch images:", err))
  }, [])

  return (
    <StatsContext.Provider value={stats}>
      <SidebarProvider
        style={
          {
            "--sidebar-width": "calc(var(--spacing) * 72)",
            "--header-height": "calc(var(--spacing) * 12)",
          } as React.CSSProperties
        }
      >
        <AppSidebar variant="inset" />
        <SidebarInset>
          <SiteHeader />
          <div className="flex flex-1 flex-col">
            <div className="@container/main flex flex-1 flex-col gap-2">
              <div className="flex flex-col gap-4 py-4 md:gap-6 md:py-6">
                <SectionCards />
                <div className="px-4 lg:px-6">
                  <ChartAreaInteractive />
                </div>
                <DataTable data={require("./data.json")} />
              </div>
            </div>
          </div>
        </SidebarInset>
      </SidebarProvider>
    </StatsContext.Provider>
  )
}