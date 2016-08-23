CEFUtils - Common Event Format Extraction Utilities
https://splunkbase.splunk.com/app/487/

The common event format is an event exchange syntax. A sample message formatted as CEF looks as follows:

CEF:0|Splunk|Test|1.0|signature:2|Test event|5|src_addr=10.0.0.0 dest_addr=20.0.0.2 src_port=32122 dest_port=80

It consists of a common prefix that always has to be present, followed by a flexible key-value extension.

In order to parse CEF data correctly in Splunk, this add-on provides 2 transforms:
 * cefHeaders - use it to extract CEF headers
 * cefKeys    - fixes multiword value extraction (by default Splunk would only extract key's values up to the first whitespace character)

The application also provides a 'cefkv' command that should be used for extracting custom keys/value pairs from CEF data - usefull if you are working with Arcsight.
Example:
CEF:0|Splunk|Test|1.0|signature:2|Test event|5|cs1=custom string value cs1Label=custom label
'cefkv' will extract following key/value pair from the sample message above:
custom_label="custom string value"

USAGE
See props.conf example supplied with the app

Thanks:
This add-on based on "Common Event Format - Field Extractions" by raffy and "jsonutils" by vbumgarner



REVISIONS:
2016/08/23 - bshuler@splunk.com
moved extractions from transforms to props
commented out TIME_FORMAT, as it was not per specification.
added extractions which perform the cefkv extractions without the needs for the command
Modified the sourcetype so that it would match cefevents and/or any sourcetype which contains :cef or :cef:
