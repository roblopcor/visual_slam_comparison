#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "lcdetector::lcdetector" for configuration "Release"
set_property(TARGET lcdetector::lcdetector APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(lcdetector::lcdetector PROPERTIES
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/liblcdetector.so"
  IMPORTED_SONAME_RELEASE "liblcdetector.so"
  )

list(APPEND _IMPORT_CHECK_TARGETS lcdetector::lcdetector )
list(APPEND _IMPORT_CHECK_FILES_FOR_lcdetector::lcdetector "${_IMPORT_PREFIX}/lib/liblcdetector.so" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
