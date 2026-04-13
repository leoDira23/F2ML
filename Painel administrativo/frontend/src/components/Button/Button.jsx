import "./button.css"

export default function Button({onClick,variant,className,children,...props}){
    return(
        <button className={`btn btn-${variant} ${className ? className : ''}`} onClick={onClick} {...props} >
            {children}
        </button>
    )
}