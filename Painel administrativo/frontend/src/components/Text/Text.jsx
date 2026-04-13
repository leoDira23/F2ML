import "./Text.css"
import React from "react"

export default function Text({as = 'span',size = 'default',color = 'default',className,children,...props}){

    const  textSize= {
        Xsmall:'textSizeXSm',
        small:'textSizeSm',
        default:'textSizeDf',
        medium:'textSizeMd',
        big:'textSizeBg'
    } 

    const textColor={
        default:"textColorBk",
        default_white:"textColorWh",
        muted:"textColorMuted"
    }
        
    return React.createElement(as,
        {
            className:`${textSize[size]} ${textColor[color]} ${className ? className : '' }`,
            ...props,
        },
        children
)
}