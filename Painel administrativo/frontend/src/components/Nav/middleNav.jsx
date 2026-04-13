import './middleNav.css'

export default function MiddleNav({children,className,...props}){
    return(
        <div className={`tablist ${className ? className : ''}`}>
            {children}
        </div>
    )
}