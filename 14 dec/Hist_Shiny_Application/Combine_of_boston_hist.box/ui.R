library(shiny)

shinyUI(fluidPage(
  
  titlePanel("plot"),
  
  sidebarLayout(
    sidebarPanel(
      selectInput(inputId="num_var",
                  label="select a variable",
                  choices=list("crim","zn","indus","chas","nox","rm","age", "dis","rad","tax","ptratio","black","lstat")),

    ),
    mainPanel(
      
      plotOutput(outputId="hist"),
      plotOutput(outputId="box")
    )
  )
))