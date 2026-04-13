import './card.css'

export default function Card({children,variant,className, ...props}){
    return (
    <div className={`card card-${variant} ${className ? className : ''}`} {...props}>
        {children}
        </div>
    )
}