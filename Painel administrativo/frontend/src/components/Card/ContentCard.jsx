import "./ContentCard.css"

export default function ContentCard({variant,children}){
    return(
        <div className={`card card-${variant}`}>
            {children}
        </div>
    )
}