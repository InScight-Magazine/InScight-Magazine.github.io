function Math(el)
  -- Replace all '|' characters with '\vert ' (trailing space prevents merging with letters)
  el.text = el.text:gsub("|", "\\vert ")
  return el
end
