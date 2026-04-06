"use client"

import { Badge } from "@/components/ui/badge"
import { useContext } from "react"
import { StatsContext } from "@/app/dashboard/page"
import {
  Card,
  CardAction,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
import { TrendingUpIcon, ImageIcon, CheckCircleIcon, AlertCircleIcon, DatabaseIcon } from "lucide-react"

export function SectionCards() {
  const { total, labeled, unlabeled, accuracy } = useContext(StatsContext)

  return (
    <div className="grid grid-cols-1 gap-4 px-4 *:data-[slot=card]:bg-gradient-to-t *:data-[slot=card]:from-primary/5 *:data-[slot=card]:to-card *:data-[slot=card]:shadow-xs lg:px-6 @xl/main:grid-cols-2 @5xl/main:grid-cols-4 dark:*:data-[slot=card]:bg-card">

      <Card className="@container/card">
        <CardHeader>
          <CardDescription>Total Images</CardDescription>
          <CardTitle className="text-2xl font-semibold tabular-nums @[250px]/card:text-3xl">
            {total}
          </CardTitle>
          <CardAction>
            <Badge variant="outline">
              <TrendingUpIcon />
              +12.5%
            </Badge>
          </CardAction>
        </CardHeader>
        <CardFooter className="flex-col items-start gap-1.5 text-sm">
          <div className="line-clamp-1 flex gap-2 font-medium">
            Growing dataset <ImageIcon className="size-4" />
          </div>
          <div className="text-muted-foreground">
            Stored in Azure Blob Storage
          </div>
        </CardFooter>
      </Card>

      <Card className="@container/card">
        <CardHeader>
          <CardDescription>Labeled Images</CardDescription>
          <CardTitle className="text-2xl font-semibold tabular-nums @[250px]/card:text-3xl">
            {labeled}
          </CardTitle>
          <CardAction>
            <Badge variant="outline">
              <TrendingUpIcon />
              +20%
            </Badge>
          </CardAction>
        </CardHeader>
        <CardFooter className="flex-col items-start gap-1.5 text-sm">
          <div className="line-clamp-1 flex gap-2 font-medium">
            {total > 0 ? Math.round((labeled / total) * 100) : 0}% labeled <CheckCircleIcon className="size-4" />
          </div>
          <div className="text-muted-foreground">
            Bounding boxes and polygons
          </div>
        </CardFooter>
      </Card>

      <Card className="@container/card">
        <CardHeader>
          <CardDescription>Unlabeled Images</CardDescription>
          <CardTitle className="text-2xl font-semibold tabular-nums @[250px]/card:text-3xl">
            {unlabeled}
          </CardTitle>
          <CardAction>
            <Badge variant="outline">
              <AlertCircleIcon />
              Pending
            </Badge>
          </CardAction>
        </CardHeader>
        <CardFooter className="flex-col items-start gap-1.5 text-sm">
          <div className="line-clamp-1 flex gap-2 font-medium">
            Needs annotation <AlertCircleIcon className="size-4" />
          </div>
          <div className="text-muted-foreground">
            {total > 0 ? Math.round((unlabeled / total) * 100) : 0}% of dataset remaining
          </div>
        </CardFooter>
      </Card>

      <Card className="@container/card">
        <CardHeader>
          <CardDescription>Annotation Accuracy</CardDescription>
          <CardTitle className="text-2xl font-semibold tabular-nums @[250px]/card:text-3xl">
            {accuracy}%
          </CardTitle>
          <CardAction>
            <Badge variant="outline">
              <TrendingUpIcon />
              +4.5%
            </Badge>
          </CardAction>
        </CardHeader>
        <CardFooter className="flex-col items-start gap-1.5 text-sm">
          <div className="line-clamp-1 flex gap-2 font-medium">
            High quality labels <DatabaseIcon className="size-4" />
          </div>
          <div className="text-muted-foreground">
            Validated by automation scripts
          </div>
        </CardFooter>
      </Card>

    </div>
  )
}