# this function take a prcomp object as input.
plot_pca <- function(pca_obj, 
                     pc_comp1 = "PC1", 
                     pc_comp2 = "PC2", 
                     meta_df, 
                     sample_id = "Sample", 
                     color = NULL, 
                     shape = NULL, 
                     label = NULL,
                     title = "PCA plot (log2 intensities)") {
  
  library(dplyr)
  library(ggplot2)
  library(ggrepel)
  library(tibble)
  
  # get PCA scores
  pca_scores <- pca_obj$x %>% as.data.frame() %>% rownames_to_column(sample_id)
  
  # get explained variance (%)
  pca_eigen_val <- round(summary(pca_obj)$importance[2, ] * 100, 1)
  
  # merge PCA scores and metadata
  pca_merged_df <- left_join(pca_scores, meta_df, by = sample_id)
  
  # build aesthetics dynamically
  aes_mapping <- aes_string(x = pc_comp1, y = pc_comp2)
  if (!is.null(color)) aes_mapping <- modifyList(aes_mapping, aes_string(color = color))
  if (!is.null(shape)) aes_mapping <- modifyList(aes_mapping, aes_string(shape = shape))
  
  # construct base plot
  p <- ggplot(pca_merged_df, aes_mapping) +
    geom_point(size = 3) +
    xlab(paste0(pc_comp1, ": ", pca_eigen_val[as.numeric(gsub("PC", "", pc_comp1))], "%")) +
    ylab(paste0(pc_comp2, ": ", pca_eigen_val[as.numeric(gsub("PC", "", pc_comp2))], "%")) +
    ggtitle(title) +
    theme_bw() +
    theme(aspect.ratio = 1, text = element_text(size = 15))+
    ggprism::scale_color_prism() +
    ggprism::scale_fill_prism()
  
  # add labels *only if provided*
  if (!is.null(label)) {
    p <- p + ggrepel::geom_text_repel(aes_string(label = label), box.padding = 0.5, max.overlaps = 20)
  }
  
  return(p)
}


plot_topN_sig_genes <- function(topN_vector,
                                normalize_mat,
                                sample_name_vector,
                                scale_rows = TRUE,
                                cluster_rows = TRUE,
                                cluster_cols = TRUE,
                                show_rownames = TRUE,
                                show_colnames = TRUE,
                                annotation_col = NULL,
                                title = "Top Significant Genes/Proteins",
                                legend_title = "Mean centered"
                                ) {
  
  # Sanity checks
  missing_genes <- setdiff(topN_vector, rownames(normalize_mat))
  missing_samples <- setdiff(sample_name_vector, colnames(normalize_mat))
  
  if (length(missing_genes) > 0) {
    warning("These genes were not found in matrix: ", paste(missing_genes, collapse = ", "))
  }
  if (length(missing_samples) > 0) {
    warning("These samples were not found in matrix: ", paste(missing_samples, collapse = ", "))
  }
  
  # Subset matrix
  selected_mat <- normalize_mat[topN_vector, sample_name_vector, drop = FALSE]
  
  # Mean-center (optional)
  if (scale_rows) {
    selected_mat <- t(scale(t(selected_mat), center = TRUE, scale = FALSE))
  }
  
  # Define color palette centered at 0
  color_limits <- range(selected_mat, na.rm = TRUE)
  color_mid <- 0
  color_breaks <- seq(color_limits[1], color_limits[2], length.out = 100)
  # colors <- colorRampPalette(c("blue", "white", "red"))(100)
  
  heatmap_legend_param = list(title = legend_title)
  
  # Plot heatmap
 p <- ComplexHeatmap::pheatmap(
    mat = selected_mat,
    # color = colors,
    breaks = color_breaks,
    cluster_rows = cluster_rows,
    cluster_cols = cluster_cols,
    show_rownames = show_rownames,
    show_colnames = show_colnames,
    annotation_col = annotation_col,
    main = title,
    heatmap_legend_param = heatmap_legend_param,
    fontsize_row = 10,
    fontsize_col = 10,
  )
  
 return (p)
}


plot_volcano <- function(df, uniq_id, pval_id, logfc_id, pval_cutoff = 0.1, show_labels = TRUE) {
  
  df <- df |> tidyr::drop_na({{pval_id}})
  df$Sig <- ifelse(df[[pval_id]] <= pval_cutoff, "Sig", "NS")
  df[[pval_id]] <- -log10(df[[pval_id]])

  p <- ggplot(df, aes(x = .data[[logfc_id]], y = .data[[pval_id]])) +
    geom_point(aes(color = Sig), size = 0.6) +
    scale_color_manual(values = c("black", "salmon")) +
    theme_bw() +
    ylab(stringr::str_glue("-log10({pval_id})")) +
    ggprism::scale_color_prism() +
    ggprism::scale_fill_prism() +
    scale_x_continuous(
      breaks = seq(
        from = floor(min(df[[logfc_id]], na.rm = TRUE)),
        to   = ceiling(max(df[[logfc_id]], na.rm = TRUE)),
        by   = 1
      )
    )

  if (show_labels) {
    top_genes <- df |>
      dplyr::arrange(.data[[pval_id]]) |>
      dplyr::slice_head(n = 10)
    p <- p + ggrepel::geom_text_repel(
      data = df |> dplyr::filter(.data[[uniq_id]] %in% top_genes[[uniq_id]]),
      aes(label = .data[[uniq_id]])
    )
  } else {
    message("Labels are disabled")
  }

  return(p)
}
