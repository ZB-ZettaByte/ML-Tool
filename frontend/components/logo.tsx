import { cn } from '../lib/utils'

export const Logo = ({ className }: { className?: string }) => {
    return (
        <div className={cn('flex items-center gap-2', className)}>
            <div style={{
                width: 32, height: 32, borderRadius: '50%',
                background: '#fff', display: 'flex',
                alignItems: 'center', justifyContent: 'center',
            }}>
                <div style={{
                    width: 10, height: 10,
                    borderRadius: '50%', background: '#000'
                }} />
            </div>
            <span style={{
                fontWeight: 700, fontSize: 18,
                color: '#fff', fontFamily: "'Syne', sans-serif"
            }}>
                AnnotateAI
            </span>
        </div>
    )
}

export const LogoIcon = ({ className }: { className?: string }) => {
    return (
        <div className={cn('flex items-center justify-center', className)} style={{
            width: 32, height: 32, borderRadius: '50%', background: '#fff'
        }}>
            <div style={{ width: 10, height: 10, borderRadius: '50%', background: '#000' }} />
        </div>
    )
}