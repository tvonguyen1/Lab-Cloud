from re import Pattern


class Constant:
    DEFAULT_ADMIN_PAGE_NUMBER = 1
    TRUE = "true"
    DEFAULT_DAILY_CRON_EXPRESSION = "0 0 * * *"
    DEFAULT_HOURLY_CRON_EXPRESSION = "0 * * * *"
    DEFAULT_INTERVAL_TIME_FOR_FS = 1000
    DEFAULT_INTERVAL_TIME_FOR_WEB = 10000
    DEFAULT_NUM_OF_THREAD_FOR_FS = 5
    DEFAULT_NUM_OF_THREAD_FOR_WEB = 1
    DEFAULT_CRAWLING_EXECUTION_INTERVAL = 5000
    USER_INFO_PROPERTY = "user.info"
    USER_FAVORITE_PROPERTY = "user.favorite"
    SEARCH_LOG_PROPERTY = "search.log"
    APPEND_QUERY_PARAMETER_PROPERTY = "append.query.parameter"
    INCREMENTAL_CRAWLING_PROPERTY = "crawling.incremental"
    CRAWLING_THREAD_COUNT_PROPERTY = "crawling.thread.count"
    CRAWLING_USER_AGENT_PROPERTY = "crawling.user.agent"
    DAY_FOR_CLEANUP_PROPERTY = "day.for.cleanup"
    WEB_API_JSON_PROPERTY = "web.api.json"
    WEB_API_SUGGEST_PROPERTY = "web.api.suggest"
    WEB_API_GSA_PROPERTY = "web.api.gsa";
    WEB_API_POPULAR_WORD_PROPERTY = "web.api.popularword";
    APP_VALUE_PROPERTY = "system.properties"
    DEFAULT_LABEL_VALUE_PROPERTY = "label.value"
    DEFAULT_SORT_VALUE_PROPERTY = "sort.value"
    VIRTUAL_HOST_VALUE_PROPERTY = "virtual.host.value"
    LOGIN_REQUIRED_PROPERTY = "login.required"
    RESULT_COLLAPSED_PROPERTY = "result.collapsed"
    LOGIN_LINK_ENALBED_PROPERTY = "login.link.enabled"
    THUMBNAIL_ENALBED_PROPERTY = "thumbnail.enabled"
    IGNORE_FAILURE_TYPE_PROPERTY = "failure.ignoretype"
    FAILURE_COUNT_THRESHOLD_PROPERTY = "failure.countthreshold"
    CSV_FILE_ENCODING_PROPERTY = "csv.file.encoding"
    PURGE_SEARCH_LOG_DAY_PROPERTY = "purge.searchlog.day"
    PURGE_USER_INFO_DAY_PROPERTY = "purge.userinfo.day"
    PURGE_JOB_LOG_DAY_PROPERTY = "purge.joblog.day"
    PURGE_BY_BOTS_PROPERTY = "purge.by.bots"
    SEARCH_FILE_PROXY_PROPERTY = "search.file.proxy"
    NOTIFICATION_TO_PROPERTY = "notification.to"
    SLACK_WEBHOOK_URLS_PROPERTY = "slack.webhook.urls"
    GOOGLE_CHAT_WEBHOOK_URLS_PROPERTY = "google.chat.webhook.urls"
    USE_BROWSER_LOCALE_FOR_SEARCH_PROPERTY = "search.use.browser.locale"
    SUGGEST_SEARCH_LOG_PROPERTY = "suggest.searchlog"
    SUGGEST_DOCUMENTS_PROPERTY = "suggest.document"
    PURGE_SUGGEST_SEARCH_LOG_DAY_PROPERTY = "purge.suggest.searchlog.day"
    LTR_MODEL_NAME_PROPERTY = "ltr.model.name"
    LTR_WINDOW_SIZE_PROPERTY = "ltr.window.size"
    REQUEST_QUERIES = "fess.Queries"
    HIGHLIGHT_QUERIES = "fess.HighlightQueries"
    FIELD_LOGS = "fess.FieldLogs";
    DEFAULT_DATETIME_FORMAT = "yyyy-MM-dd'T'HH:mm:ss";
    ISO_DATETIME_FORMAT = "yyyy-MM-dd'T'HH:mm:ss.SSS'Z'"
    DATE_OPTIONAL_TIME = "date_optional_time"
    DONE_STATUS = 9999
    '''DEFAULT_IGNORE_FAILURE_TYPE = StringUtil.EMPTY'''
    DEFAULT_FAILURE_COUNT = -1
    DEFAULT_PURGE_DAY = "-1"
    DEFAULT_SUGGEST_PURGE_DAY = "30"
    DEFAULT_PURGE_BY_BOTS = "Crawler" // + ",crawler" // + ",Bot" // + ",bot" // + ",ia_archiver" // + ",Seznam" // + ",Google Desktop"
    DEFAULT_FROM_EMAIL = "Administrator <root@localhost>";
    CRAWLER_STATUS = "CrawlerStatus"
    CRAWLER_ERRORS = "CrawlerErrors"
    SESSION_ID = "sessionId"
    CRAWLING_INFO_ID = "crawlingInfoId"
    INDEXING_TARGET = "indexingTarget"
    NUM_OF_THREADS = "numOfThreads"
    BASIC = "BASIC"
    DIGEST = "DIGEST"
    NTLM = "NTLM"
    FORM = "FORM"
    SAMBA = "SAMBA"
    FTP = "FTP"
    RESERVED = {"\\", "+", "-", "&&", "||", "!", "(", ")", "{", "}", "[", "]", "^", "~", "*", "?", ";", ":", "/"}
    LUCENE_FIELD_RESERVED_PATTERN = Pattern.compile("([+\\-!\\(\\){}\\[\\]^\"~\\\\:\\p{Zs}]|(&&)|(\\|\\|))") // "*", "?",
    LUCENE_RANGE_FIELD_RESERVED_PATTERN = Pattern.compile("([!\\(\\){}\\[\\]\"~\\\\:\\p{Zs}]|(&&)|(\\|\\|))")
    SEARCH_LOG_ACCESS_TYPE = "searchLogAccessType"
    SEARCH_LOG_ACCESS_TYPE_JSON = "json"
    SEARCH_LOG_ACCESS_TYPE_GSA = "gsa"
    SEARCH_LOG_ACCESS_TYPE_WEB = "web"
    SEARCH_LOG_ACCESS_TYPE_ADMIN = "admin"
    SEARCH_LOG_ACCESS_TYPE_OTHER = "other"
    RESULTS_PER_PAGE = "resultsPerPage"
    USER_CODE = "userCode"
    SEARCH_FIELD_LOG_SEARCH_QUERY = "q"
    STATS_REPORT_TYPE = "reportType"
    RESULT_DOC_ID_CACHE = "resultDocIds"
    CRAWLING_INFO_SYSTEM_NAME = "system"
    '''view parameters'''
    FACET_QUERY = "fess.FacetQuery"
    GEO_QUERY = "fess.GeoQuery"
    FACET_FORM = "fess.FacetForm"
    GEO_FORM = "fess.GeoForm"
    LABEL_VALUE_MAP = "fess.LabelValueMap"
    OPTION_QUERY_Q = "q"
    OPTION_QUERY_CQ = "cq"
    OPTION_QUERY_OQ = "oq"
    OPTION_QUERY_NQ = "nq"

    SCHEDULED_JOB = "scheduledJob"
    DEFAULT_JOB_TARGET = "all"
    DEFAULT_JOB_SCRIPT_TYPE = "groovy"
    EXIT_OK = 0
    EXIT_FAIL = 1
    DCF = "dcf"
    ALL_LANGUAGES = "all"
    INVALID_NUMERIC_PARAMETER = "-1"
    FACET_FIELD_PREFIX = "field:"
    FACET_QUERY_PREFIX = "query:"
    MATCHES_ALL_QUERY = "*:*"
    FESS_ES_HTTP_ADDRESS = "fess.es.http_address"
    DEFAULT_PAGE_SIZE = 20
    DEFAULT_START_COUNT = 0
    PROCESS_TYPE_REPLACE = "R"
    PROCESS_TYPE_CRAWLING = "C"
    PROCESS_TYPE_DISPLAYING = "D"
    PROCESS_TYPE_BOTH = "B"
    PAGER_CONVERSION_RULE = {"allRecordCount", "pageSize", "currentPageNumber", "allPageCount", "existPrePage", "existNextPage"}
    WEB_CRAWLER_TYPE = "web_crawling"
    FILE_CRAWLER_TYPE = "file_crawling"
    DATA_CRAWLER_TYPE = "data_crawling"
    COMMON_CONVERSION_RULE = {"crudMode", "createdBy", "createdTime", "updatedBy", "updatedTime"}
    COMMON_API_CONVERSION_RULE = {"crudMode"}
    USER_INFO = "LoginInfo"
    ES_API_ACCESS_TOKEN = "esApiAccessToken"
    DEFAULT_FIELD = "_default"
    DEFAULT_DAY_FOR_CLEANUP = 3
    FESS_CONF_PATH = "fess.conf.path"
    LDAP_BASE_DN = "ldap.base.dn"
    LDAP_SECURITY_PRINCIPAL = "ldap.security.principal"
    LDAP_ADMIN_SECURITY_PRINCIPAL = "ldap.admin.security.principal"
    LDAP_ADMIN_SECURITY_CREDENTIALS = "ldap.admin.security.credentials"
    LDAP_PROVIDER_URL = "ldap.provider.url"
    LDAP_SECURITY_AUTHENTICATION = "ldap.security.authentication"
    LDAP_INITIAL_CONTEXT_FACTORY = "ldap.initial.context.factory"
    LDAP_ACCOUNT_FILTER = "ldap.account.filter"
    LDAP_GROUP_FILTER = "ldap.group.filter"
    LDAP_MEMBEROF_ATTRIBUTE = "ldap.memberof.attribute"
    NOTIFICATION_LOGIN = "notification.login"
    NOTIFICATION_SEARCH_TOP = "notification.search.top"
    NOTIFICATION_ADVANCE_SEARCH = "notification.advance.search"
    STORAGE_ENDPOINT = "storage.endpoint"
    STORAGE_ACCESS_KEY = "storage.accesskey"
    STORAGE_SECRET_KEY = "storage.secretkey"
    STORAGE_BUCKET = "storage.bucket"
    MAPPING_TYPE_ARRAY = "array"
    MAPPING_TYPE_STRING = "string"
    MAPPING_TYPE_LONG = "long"
    MAPPING_TYPE_DOUBLE = "double"
    MAPPING_TYPE_DATE = "date"
    MAPPING_TYPE_PDF_DATE = "pdf_date"
    PAGING_QUERY_LIST = "pagingQueryList"
    REQUEST_LANGUAGES = "requestLanguages"
    SEARCH_PREFERENCE_LOCAL = "_local"
    GSA_API_VERSION = "3.2"
    PERMISSIONS = "permissions"
    QUERIES = "queries"
    VIRTUAL_HOSTS = "virtualHosts"
    CIPHER_PREFIX = "{cipher}"
    SYSTEM_USER = "system"
    EMPTY_USER_ID = "<empty>"
    CRAWLER_PROCESS_COMMAND_THREAD_DUMP = "thread_dump"
    FESS_THUMBNAIL_PATH = "fess.thumbnail.path"
    FESS_VAR_PATH = "fess.var.path"
    FESS_LOG_LEVEL = "fess.log.level"
    TRACK_TOTAL_HITS = "track_total_hits"
    SYSTEM_PROP_PREFIX = "fess.system."
    FESS_CONFIG_PREFIX = "fess.config."
    XERCES_FEATURE_PREFIX = "http://apache.org/xml/features/"
    LOAD_EXTERNAL_DTD_FEATURE = "nonvalidating/load-external-dtd"
    EXECUTE_TYPE_CRAWLER = "crawler"
    EXECUTE_TYPE_THUMBNAIL = "thumbnail"
    EXECUTE_TYPE_PYTHON = "python"
    EXECUTE_TYPE_SUGGEST = "suggest"
    DEFAULT_SCRIPT = "groovy"
    TEXT_FRAGMENTS = "text_fragments"
    TEXT_FRAGMENT_TYPE_QUERY = "query"
    TEXT_FRAGMENT_TYPE_HIGHLIGHT = "highlight"





