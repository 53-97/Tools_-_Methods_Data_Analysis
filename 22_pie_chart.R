# Define the data
sectors <- c("Agriculture", "Industry", "Services")

# India 1990
india_1990 <- c(70, 15, 15)
# India 2022
india_2022 <- c(45, 20, 35)
# Germany 1990
germany_1990 <- c(5, 30, 65)
# Germany 2022
germany_2022 <- c(2, 13, 85)

# Set up the plotting area: 2 rows x 2 columns
par(mfrow = c(2, 2))

# Pie chart for India 1990
pie(india_1990, labels = paste(sectors, india_1990, "%"), 
    main = "India - 1990", col = c("#66c2a5", "#fc8d62", "#8da0cb"))

# Pie chart for India 2022
pie(india_2022, labels = paste(sectors, india_2022, "%"), 
    main = "India - 2022", col = c("#66c2a5", "#fc8d62", "#8da0cb"))

# Pie chart for Germany 1990
pie(germany_1990, labels = paste(sectors, germany_1990, "%"), 
    main = "Germany - 1990", col = c("#66c2a5", "#fc8d62", "#8da0cb"))

# Pie chart for Germany 2022
pie(germany_2022, labels = paste(sectors, germany_2022, "%"), 
    main = "Germany - 2022", col = c("#66c2a5", "#fc8d62", "#8da0cb"))

# Reset plotting layout
par(mfrow = c(1, 1))
