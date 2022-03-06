#!/usr/bin/env Rscript
#############################################
# @ Author: Chen Jun
# @ Author Email: 1170101471@qq.com
# @ Created Date: 2022-03-06, 19:51:59
# @ Modified By: Chen Jun
# @ Last Modified: 2022-03-06, 19:56:00
#############################################


source("/home/chenjun/pipeline/mRNA/script/tools_DE_analysis/PCA/PCA.R")

data <- read.table("./a.txt", header = T, row.names = 1)
groups <- colnames(data)

outname <- "pca_a.showtext"
geomtext <- TRUE
# data$Species <- groups
# write.csv(data, "test.csv")
# plot(gene1 = data[1, ], gene2 = data[2, ])
# plot_PCA(data = data, groups = groups, outname = "pca_iris", geomtext = FALSE)
plot_PCA(data = data, groups = groups, outname = outname, geomtext = geomtext)
