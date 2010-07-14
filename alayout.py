import cgi

class ALayout(object):
	nestStack = []
	
	@property
	def tagname(self):
		return self.__class__.__name__
	
	def __init__(self, **kwargs):
		self.attrs = kwargs
		self.body = []
		self.entered = False
		
		if len(ALayout.nestStack):
			parent = ALayout.nestStack[-1]
			if not parent.entered:
				ALayout.nestStack.pop()
			else:
				parent.body.append(self)
		ALayout.nestStack.append(self)
	
	def __enter__(self, *args, **kwargs):
		self.entered = True
		return self
	
	def __exit__(self, *args, **kwargs):
		while len(ALayout.nestStack):
			val = ALayout.nestStack.pop()
			if len(ALayout.nestStack) == 0:
				val['xmlns:android'] = 'http://schemas.android.com/apk/res/android'
				print '<?xml version="1.0" encoding="utf-8"?>'
				print val
			if val.entered:
				break
	
	def __getitem__(self, name):
		return self.attrs[name]
	def __setitem__(self, name, value):
		self.attrs[name] = value
	
	def __str__(self):
		tag = '<%s' % self.tagname
		for k, v in self.attrs.items():
			ns = '' if ':' in k else 'android:'
			tag += ' %s%s="%s"' % (ns, k, cgi.escape(v))
		if len(self.body):
			tag += '>'
			tag += '\n'.join(map(str, self.body))
			tag += '</%s>' % self.tagname
		else:
			tag += '/>'
		return tag

tags = 'AnalogClock, ImageView, KeyboardView, ProgressBar, SurfaceView, TextView, ViewGroup, ViewStub, AbsListView, AbsSeekBar, AbsSpinner, AbsoluteLayout, AppWidgetHostView, AutoCompleteTextView, Button, CheckBox, CheckedTextView, Chronometer, CompoundButton, DatePicker, DialerFilter, DigitalClock, EditText, ExpandableListView, ExtractEditText, FrameLayout, GLSurfaceView, Gallery, GestureOverlayView, GridView, HorizontalScrollView, ImageButton, ImageSwitcher, LinearLayout, ListView, MediaController, MultiAutoCompleteTextView, QuickContactBadge, RadioButton, RadioGroup, RatingBar, RelativeLayout, ScrollView, SeekBar, SlidingDrawer, Spinner, TabHost, TabWidget, TableLayout, TableRow, TextSwitcher, TimePicker, ToggleButton, TwoLineListItem, VideoView, ViewAnimator, ViewFlipper, ViewSwitcher, WebView, ZoomButton, ZoomControls'.split(', ')
for tag in tags:
	globals()[tag] = type(tag, (ALayout, ), {})
