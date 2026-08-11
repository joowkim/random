theme_publication <- theme_classic() +
  theme(
    text = element_text(family = "Arial", size = 10),
    axis.title = element_text(size = 11),
    axis.text = element_text(size = 9, color = "black"),
    legend.title = element_text(size = 10),
    legend.text = element_text(size = 9),
    legend.position = "bottom",
    strip.text = element_text(size = 10, face = "bold"),
    panel.grid = element_blank(),
    axis.line = element_line(size = 0.5),
    axis.ticks = element_line(size = 0.5)
  )
